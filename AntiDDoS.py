import sys
import time
import requests
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFormLayout, QMessageBox
from PyQt5.QtCore import Qt
from flask import Flask, request, abort, Response

# Flask app and DDoS protection settings
REAL_SITE = ""
RATE_LIMIT = 30
BAN_TIME = 300
PORT = 8080

ip_logs = {}
banned = {}

UA_BLACKLIST = ["python-requests", "curl", "wget", "scraper", "bot", "scan"]

def is_bot():
    ua = request.headers.get("User-Agent", "").lower()
    return any(bad in ua for bad in UA_BLACKLIST)

def is_banned(ip):
    if ip in banned and time.time() < banned[ip]:
        return True
    return False

# Flask request control (Rate Limiting and Bot Control)
app = Flask(__name__)

@app.before_request
def protection():
    ip = request.remote_addr
    now = time.time()

    # Bot detection
    if is_bot():
        banned[ip] = now + BAN_TIME
        abort(403)

    # Ban detection
    if is_banned(ip):
        abort(403)

    # Rate Limit
    if ip not in ip_logs:
        ip_logs[ip] = []
    ip_logs[ip] = [t for t in ip_logs[ip] if now - t < 1]

    if len(ip_logs[ip]) > RATE_LIMIT:
        banned[ip] = now + BAN_TIME
        abort(403)

    ip_logs[ip].append(now)

# Proxy routing (redirecting traffic to the real site)
@app.route('/', defaults={'path': ''}, methods=["GET", "POST"])
@app.route('/<path:path>', methods=["GET", "POST"])
def proxy(path):
    url = f"{REAL_SITE}/{path}"

    try:
        if request.method == "GET":
            resp = requests.get(url, headers=request.headers, params=request.args, timeout=5)
        else:
            resp = requests.post(url, headers=request.headers, data=request.form, timeout=5)
    except:
        abort(503)

    headers = [(k, v) for (k, v) in resp.headers.items() if k.lower() not in ["content-encoding", "content-length"]]
    return Response(resp.content, resp.status_code, headers)

# Run Flask app in the background
def run_flask():
    app.run(host="0.0.0.0", port=PORT)

# PyQt5 GUI implementation
class AntiDDoSApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aury WebShield - Anti-DDoS Firewall')
        self.setGeometry(100, 100, 500, 400)
        
        # Layout setup
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.url_input = QLineEdit()
        form_layout.addRow('Target Site URL:', self.url_input)

        self.rate_limit_input = QLineEdit("30")
        form_layout.addRow('Rate Limit (req/sec):', self.rate_limit_input)

        self.ban_time_input = QLineEdit("300")
        form_layout.addRow('Ban Duration (seconds):', self.ban_time_input)

        self.port_input = QLineEdit("8080")
        form_layout.addRow('Firewall Port:', self.port_input)

        layout.addLayout(form_layout)

        # Buttons
        self.start_button = QPushButton('Start WebShield Firewall')
        self.start_button.clicked.connect(self.start_firewall)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton('Stop WebShield Firewall')
        self.stop_button.clicked.connect(self.stop_firewall)
        layout.addWidget(self.stop_button)

        # Logs area
        self.logs_label = QLabel("Blocked IPs:")
        layout.addWidget(self.logs_label)

        self.logs_text = QTextEdit()
        self.logs_text.setReadOnly(True)
        layout.addWidget(self.logs_text)

        self.view_logs_button = QPushButton('View Logs')
        self.view_logs_button.clicked.connect(self.view_logs)
        layout.addWidget(self.view_logs_button)

        self.setLayout(layout)

    def start_firewall(self):
        global REAL_SITE, RATE_LIMIT, BAN_TIME, PORT

        REAL_SITE = self.url_input.text()
        RATE_LIMIT = int(self.rate_limit_input.text())
        BAN_TIME = int(self.ban_time_input.text())
        PORT = int(self.port_input.text())

        if not REAL_SITE.startswith("http"):
            QMessageBox.critical(self, "Error", "Please enter a valid URL!")
            return

        # Start Flask app in a separate thread
        threading.Thread(target=run_flask, daemon=True).start()

        QMessageBox.information(self, "Started", "WebShield Firewall is running.")

    def stop_firewall(self):
        subprocess.call(["killall", "python3"])  # Stop the Python process
        QMessageBox.information(self, "Stopped", "WebShield Firewall stopped.")

    def view_logs(self):
        try:
            with open("banned_ips.txt", "r") as f:
                logs = f.readlines()
            self.logs_text.clear()
            self.logs_text.append("".join(logs))
        except FileNotFoundError:
            self.logs_text.clear()
            self.logs_text.append("No banned IPs found.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AntiDDoSApp()
    window.show()
    sys.exit(app.exec_())
