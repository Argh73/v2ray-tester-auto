#!/usr/bin/env python3
import asyncio
import sys
from pathlib import Path

# Import from the package
sys.path.insert(0, str(Path(__file__).parent))

from v2ray_tester.subs import load_subs, fetch_all_subs
from v2ray_tester.options import TestOptions
from v2ray_tester.process import find_xray
import v2ray_tester.tester as tester_module

async def main():
 print("🚀 Starting headless V2Ray tester with limit...")

 xray_path = find_xray()
 if not xray_path:
 print("❌ Xray not found!")
 return

 opts = TestOptions()
 opts.live_output = False
 opts.speed_size = 2 * 1024 * 1024 
 
 MAX_GOOD = 800

 print(f"Target: Stop after {MAX_GOOD} good configs")

 subs = load_subs()
 if not subs:
 print("No subs in subs.txt")
 return

 print(f"Found {len(subs)} subscription link(s)")

 # Fetch configs
 links, _, _ = await fetch_all_subs(subs, concurrency=20)
 print(f"Extracted {len(links)} configs")

 if len(links) == 0:
 return

 print("Starting bulk test with limit...")

 try:
 import subprocess
 result = subprocess.run([
 "python", "v2ray-bulk-tester.py",
 "-i", "subs.txt",
 "-o", "Test.txt",
 "-c", "25"
 ], timeout=1200, capture_output=True, text=True) # 20 دقیقه
 
 print(result.stdout)
 except subprocess.TimeoutExpired:
 print("⏰ Time limit reached. Stopping...")

 print(f"✅ Process finished. Check Test.txt (target was {MAX_GOOD} good configs)")

if __name__ == "__main__":
 asyncio.run(main())
