# 🛡️ AurySoftWare© AntiDDoS WebShield — Anti‑DDoS Firewall & Reverse Proxy  
![Logo](https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Aury WebShield is an **Anti‑DDoS firewall** written in **Python** using **PyQt5** for the GUI.  
It works as a **reverse proxy** for real websites and filters incoming traffic through various security layers:
<img width="498" height="430" alt="image" src="https://github.com/user-attachments/assets/e61d1560-4c9a-439e-ba55-f44978fc835d" />

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
Bu uygulama tamamen açık kaynak Python kodudur. 
Virüs uyarısı; exe dosyasının nasıl derlendiğinden (PyInstaller) kaynaklanan yaygın bir false positive’tir. 
Kodun tamamı GitHub’da açıktır, inceleyebilirsiniz. 
Microsoft Defender, Kaspersky, ESET, Bitdefender dahil 67+ antivirüs temiz dedi.


Aury Anti‑DDoS, web sitelerini savunma amacıyla geliştirilmiş bir güvenlik aracıdır ve yalnızca trafik filtresi yapmak, güvenlik duvarı işlevi görmek ve DDoS koruması sağlamak için kullanılmalıdır. Yazılım başka sistemlere izinsiz müdahalede bulunmak, saldırı başlatmak, trafik gönderme veya herhangi bir sisteme zarar verme amacıyla kullanılamaz.

Bu yazılım yalnızca:

Kendi sahip olduğunuz web sitelerinde,

İzin aldığınız sistemlerde,

Test, geliştirme ve eğitim amaçlı ortamlar gibi izinli alanlarda kullanılmalıdır.

Bu yazılımı kullanarak, kullanıcı:

Yazılımın yalnızca savunma amaçlı olduğunu,

Kendi sorumluluğunda kullanılması gerektiğini kabul eder.

Geliştirici ve yayıncı, yazılımın kötüye kullanımından, izinsiz sistemlerde kullanılmasından veya herhangi bir şekilde yasal olmayan bir işlem yapılmasından dolayı sorumlu tutulamaz. Ayrıca, yazılımın yanlış yapılandırılması veya hatalı kullanımından kaynaklanabilecek herhangi bir zarar ve hukuki sorumluluktan tamamen bağımsızdır.

Uyarı: Yazılım, yerel yasal düzenlemelere ve etik kurallara uygun şekilde kullanılmalıdır. Yazılımı kullanan kişi, sorumluluklarının farkında olmalı ve yasal izinlere sahip olmalıdır.

🇺🇸 English Disclaimer:

Aury Anti‑DDoS is a defensive security tool designed to protect websites by filtering traffic, acting as a firewall, and providing DDoS protection. The software must not be used to interfere with, attack, flood, or disrupt any system.

This software is intended solely for use on:

Your own websites,

Systems where you have explicit permission,

Test, development, and educational environments that are authorized for use.

By using this software, the user acknowledges that:

The software is intended for defensive purposes only.

The user assumes full responsibility for its usage.

The developer and publisher assume no liability for any misuse, unauthorized use, or any illegal activities performed using this software. Additionally, they are not responsible for any damages or legal consequences resulting from improper configuration or incorrect usage of the software.

Warning: This software should only be used in compliance with local laws, ethical guidelines, and with proper permissions. The user must ensure they have the necessary legal authorizations to use the software.
