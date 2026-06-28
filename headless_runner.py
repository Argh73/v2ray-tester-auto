#!/usr/bin/env python3
print("🚀 Simple Test Runner Started")

import subprocess
import time
from pathlib import Path

# ساخت subs.txt
with open("subs.txt", "w") as f:
    f.write("https://raw.githubusercontent.com/Argh73/VpnConfigCollector/refs/heads/main/All_Configs_Sub.txt\n")

print("✅ subs.txt created")

# فقط تست اجرای bulk tester
print("Running v2ray-bulk-tester...")

try:
    result = subprocess.run(
        ["python", "v2ray-bulk-tester.py", "-i", "subs.txt", "-o", "Test.txt", "-c", "10"],
        timeout=600,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print("ERROR:", result.stderr)
except Exception as e:
    print("Exception:", str(e))

print("Runner finished.")
print("Test.txt exists?", Path("Test.txt").exists())
