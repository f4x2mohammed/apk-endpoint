import argparse
import subprocess
import tempfile
import shutil
import re
import os
from pathlib import Path

USER = "f4x2mohammed"

def run_apktool(apk_path, out_dir):
    try:
        print(f"[+] Decompiling APK: {apk_path}")
        subprocess.run(
            ["apktool", "d", "-f", apk_path, "-o", out_dir],
            check=True,
            capture_output=True,
            text=True
        )
        print("[+] Decompile finished.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[!] Apktool error:\n{e.stderr}")
        return False

def extract_urls_from_file(file_path):
    urls = set()
    url_regex = re.compile(r"https?://[^\s\"\'<>]+")
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                urls.update(url_regex.findall(line))
    except Exception:
        pass
    return urls

def extract_smart_endpoints(root_dir):
    keywords = ['api', 'endpoint', 'base_url', 'host', 'url', 'server']
    found = set()
    for dirpath, _, files in os.walk(root_dir):
        for filename in files:
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read().lower()
                    lines = content.splitlines()
                    for line in lines:
                        for kw in keywords:
                            if kw in line:
                               
                                matches = re.findall(r"https?://[^\s\"\'<>]+", line)
                                for m in matches:
                                    found.add(m.strip())
                                
                                if not matches:
                                    parts = re.split(r"[=:\"]", line)
                                    for part in parts:
                                        part = part.strip()
                                        if part.startswith("http"):
                                            found.add(part)
            except:
                continue
    return found

def extract_urls(root_dir):
    all_urls = set()
    for dirpath, _, files in os.walk(root_dir):
        for filename in files:
            filepath = os.path.join(dirpath, filename)
            urls = extract_urls_from_file(filepath)
            all_urls.update(urls)
    return all_urls

def main():
    parser = argparse.ArgumentParser(description=f"APK URL Extractor by {USER}")
    parser.add_argument("-a", "--apk", required=True, help="APK file path")
    parser.add_argument("-o", "--output", default="allurls.txt", help="Output URLs file")
    parser.add_argument("--keep", action="store_true", help="Keep decompiled folder")
    args = parser.parse_args()

    apk_path = Path(args.apk)
    if not apk_path.is_file():
        print(f"[!] APK file not found: {apk_path}")
        return

    temp_dir = tempfile.mkdtemp(prefix="f4x2apk_")
    print(f"[+] Using temp folder: {temp_dir}")

    if not run_apktool(str(apk_path), temp_dir):
        shutil.rmtree(temp_dir)
        return

    print("[+] Extracting URLs from all files...")
    urls = extract_urls(temp_dir)

    print("[+] Extracting smart endpoints...")
    smart_urls = extract_smart_endpoints(temp_dir)

    combined = urls.union(smart_urls)

    if combined:
        with open(args.output, "w") as f:
            for url in sorted(combined):
                f.write(url + "\n")
        print(f"[+] Extracted {len(combined)} URLs saved to {args.output}")
    else:
        print("[!] No URLs found.")

    if args.keep:
        print(f"[+] Decompiled folder kept at: {temp_dir}")
    else:
        shutil.rmtree(temp_dir)
        print("[+] Temporary folder cleaned up.")

if __name__ == "__main__":
    main()
