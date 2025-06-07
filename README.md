# 🔍 APK Endpoint Extractor

**apk-endpoint.py** is a lightweight, intelligent tool designed to extract external endpoints (URLs) from Android APK files. It combines static analysis using `apktool` and `androguard`, with smart filtering to give you valuable bug bounty and security insights.

---

## 🚀 Features

- 🧠 Smart static analysis with AI-enhanced string search
- 🛠️ Decompile APKs using apktool
- 📦 Extract from smali, XML, JSON, JS, HTML, and more
- 📚 Analyze DEX bytecode with Androguard
- 🔒 Filters out private IPs and localhost links
- 🧼 Automatically cleans up temporary files
- 💡 CLI-only – fast, focused, and minimal

---

## 📦 Requirements

Install required tools:

```bash
sudo apt update
sudo apt install apktool python3-pip -y
pip install androguard

## ⚙️ Usage
python3 apk-endpoint.py -a app.apk -o urls.txt

👨‍💻 Author
Developed with ❤️ by f4x2mohammed


