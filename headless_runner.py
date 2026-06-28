#!/usr/bin/env python3
print("=== V2RAY TEST RUNNER STARTED ===")
print("Current time:", __import__('time').strftime("%Y-%m-%d %H:%M:%S"))

with open("subs.txt", "w") as f:
    f.write("https://raw.githubusercontent.com/Argh73/VpnConfigCollector/refs/heads/main/All_Configs_Sub.txt\n")

print("subs.txt created successfully")

print("Trying to run bulk tester...")
try:
    import subprocess
    result = subprocess.run(["python", "--version"], capture_output=True, text=True)
    print("Python version:", result.stdout.strip())

    print("Running v2ray-bulk-tester.py ...")
    result = subprocess.run(
        ["python", "v2ray-bulk-tester.py", "-i", "subs.txt", "-o", "Test.txt", "-c", "5"],
        timeout=300,
        capture_output=True,
        text=True
    )
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("Return code:", result.returncode)
except Exception as e:
    print("ERROR occurred:", str(e))

print("=== RUNNER FINISHED ===")
