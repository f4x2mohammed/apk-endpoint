# APK Endpoint Extractor

**apk-endpoint.py** is a lightweight, intelligent Python tool designed to extract external endpoints (URLs) from Android APK files. It uses static analysis by decompiling APKs with `apktool` and performs smart keyword-based extraction from the source files.

---

## 🚀 Features

- Decompile APK files using `apktool`
- Extract URLs from various files inside the APK (XML, smali, JSON, JS, etc.)
- Smart extraction based on common keywords like `api`, `endpoint`, `base_url`, `host`, `url`, and `server`
- Option to keep or delete the temporary decompiled folder
- Easy CLI interface

---

## 📦 Requirements

- Python 3.x
- `apktool` installed and available in your system PATH
- Python package: `argparse` (usually included in standard Python)
- Linux or Windows environment with Python and apktool installed

---

## ⚙️ Installation

1. Install apktool:

```bash
sudo apt update && sudo apt install apktool -y
```

💻 Usage
Command:
```bash
python3 apk-endpoint.py -a /path/to/app.apk -o extracted_urls.txt
```

👨‍💻 Author
Developed with ❤️ by f4x2mohammed



