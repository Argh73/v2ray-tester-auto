#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path
import time

print("="*60)
print("🚀 V2Ray Headless Runner - Debug Mode")
print("="*60)

# چک کردن فایل‌ها
print("📁 Current directory files:")
print(list(Path(".").glob("*")))

# چک Xray
print("\n🔍 Checking Xray...")
xray_dir = Path("xray-linux-64")
if xray_dir.exists():
    xray_bin = xray_dir / "xray"
    if xray_bin.exists():
        print(f"✅ Xray found at {xray_bin}")
        subprocess.run(["ls", "-la", str(xray_bin)])
    else:
        print("❌ xray binary not found inside folder")
else:
    print("❌ xray-linux-64 folder not found")

# ساخت subs.txt
print("\n📝 Creating subs.txt...")
raw_url = "https://raw.githubusercontent.com/Argh73/VpnConfigCollector/refs/heads/main/All_Configs_Sub.txt"
with open("subs.txt", "w") as f:
    f.write(raw_url + "\n")
print(f"✅ subs.txt created with: {raw_url}")

# اجرای Bulk Tester
print("\n🔄 Running v2ray-bulk-tester.py ...")
try:
    start = time.time()
    result = subprocess.run(
        ["python", "v2ray-bulk-tester.py", "-i", "subs.txt", "-o", "Test.txt", "-c", "15"],
        timeout=900,          # 15 دقیقه
        capture_output=True,
        text=True,
        cwd=str(Path("."))
    )
    print(f"⏱️  Finished in {time.time()-start:.1f} seconds")
    print("\n=== STDOUT ===")
    print(result.stdout)
    if result.stderr:
        print("\n=== STDERR ===")
        print(result.stderr)
    print(f"Return code: {result.returncode}")

except subprocess.TimeoutExpired:
    print("⏰ Timeout reached")
except FileNotFoundError:
    print("❌ v2ray-bulk-tester.py not found!")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

# نتیجه نهایی
test_file = Path("Test.txt")
if test_file.exists():
    lines = test_file.read_text(encoding="utf-8", errors="ignore").count("\n")
    print(f"\n✅ Test.txt created with ~{lines} lines")
else:
    print("\n❌ Test.txt was NOT created!")

print("\n🏁 Runner finished")
