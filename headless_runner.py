
import asyncio
import sys
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from v2ray_tester.subs import load_subs
from v2ray_tester.process import find_xray


async def run_headless():
    print("🚀 Starting Headless V2Ray Tester with Limit")

    xray_path = find_xray()
    if not xray_path:
        print("❌ Xray core not found!")
        return 1

    print(f"✅ Xray found: {xray_path}")

    subs = load_subs()
    print(f"📋 Loaded {len(subs)} subscription link(s)")

    MAX_GOOD_CONFIGS = 800  
    MAX_TIME_MINUTES = 25

    print(f"🎯 Target: Stop after {MAX_GOOD_CONFIGS} good configs or {MAX_TIME_MINUTES} minutes")

    try:
        # اجرای Bulk Tester با محدودیت زمانی
        process = subprocess.run(
            [
                "python", "v2ray-bulk-tester.py",
                "-i", "subs.txt",
                "-o", "Test.txt",
                "-c", "25"        
            ],
            timeout=MAX_TIME_MINUTES * 60,
            capture_output=True,
            text=True
        )
        
        print(process.stdout)
        if process.stderr:
            print("Errors:", process.stderr)

    except subprocess.TimeoutExpired:
        print(f"⏰ Time limit ({MAX_TIME_MINUTES} minutes) reached. Stopping...")
    except Exception as e:
        print(f"❌ Error: {e}")

    if Path("Test.txt").exists():
        good_count = sum(1 for line in open("Test.txt") if line.strip())
        print(f"✅ Finished! Total good configs in Test.txt: {good_count}")
    else:
        print("⚠️ Test.txt not created")

    return 0


if __name__ == "__main__":
    asyncio.run(run_headless())
