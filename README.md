# 🛡️ Aury WebShield — Anti‑DDoS Firewall & Reverse Proxy  
![Logo](https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Aury WebShield is an **Anti‑DDoS firewall** written in **Python** using **PyQt5** for the GUI.  
It works as a **reverse proxy** for real websites and filters incoming traffic through various security layers:

✔ **Rate Limit (requests per second)**  
✔ **IP Ban**  
✔ **Bot Detection**  
✔ **Proxy Filtering**

The project is designed with a **user-friendly GUI**, making it suitable for use even by businesses or larger organizations.

---

# 🚀 Features

### 🖥️ User Interface (PyQt5)
- Set target site URL
- Define rate limit
- Set ban duration
- Configure firewall port
- View logs of blocked IPs

### 🛡️ Security Layers
- **User-Agent** bot detection
- **Rate Limit** (requests per second per IP)
- **IP Banning** after exceeding rate limit
- **Reverse Proxy** to hide the real target site
- Logs of banned IPs saved to file

### 🔥 Backend
- Reverse Proxy with **Flask**
- Fully self-contained in a single file
- Cross-platform: Windows, Linux, and macOS compatible

---

# 📦 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/Aury-WebShield
cd Aury-WebShield
