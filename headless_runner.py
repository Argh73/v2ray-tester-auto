#!/usr/bin/env python3
import asyncio
import sys
import subprocess
from pathlib import Path

print("🚀 Starting Simple Headless V2Ray Tester")

# اضافه کردن مسیر
sys.path.insert(0, str(Path(__file__).parent))

try:
    from v2ray_tester.process import find_xray
    xray = find_xray()
    print(f"✅ Xray found: {xray}")
except Exception as e:
    print(f"❌ Error finding Xray: {e}")

# ایجاد subs.txt
with open("subs.txt", "w") as f:
    f.write("https://raw.githubusercontent.com/Argh73/VpnConfigCollector/refs/heads/main/All_Configs_Sub.txt\n")

print("✅ subs.txt created with your link")

# اجرای تست با bulk tester
print("🔄 Running v2ray-bulk-tester...")
try:
    result = subprocess.run([
        "python", "v2ray-bulk-tester.py",
        "-i", "subs.txt",
        "-o", "Test.txt",
        "-c", "20"
    ], timeout=1800, text=True, capture_output=True)   # 30 دقیقه

    print("=== Output ===")
    print(result.stdout)
    if result.stderr:
        print("=== Errors ===")
        print(result.stderr)

except subprocess.TimeoutExpired:
    print("⏰ Time limit reached")
except Exception as e:
    print(f"Error: {e}")

# چک کردن نتیجه
test_file = Path("Test.txt")
if test_file.exists() and test_file.stat().st_size > 0:
    count = len([line for line in open(test_file) if line.strip()])
    print(f"✅ Success! {count} good configs saved in Test.txt")
else:
    print("⚠️ No Test.txt created or it's empty")
    # سعی دوم با main.py
    print("Trying main.py --auto ...")
    try:
        subprocess.run(["python", "main.py", "--auto"], timeout=600)
    except:
        pass
