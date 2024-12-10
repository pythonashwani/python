#!/usr/bin/python3
import subprocess

# result = subprocess.run(["ls -ltra"], shell=True, capture_output=True, text=True)
result = subprocess.run(["python", "50_os_0_cwd1.py"], capture_output=True, text=True, check=False)

print(result.stdout)
print(result.stderr)


return_code = subprocess.call(["python", "--version"])

if return_code == 0:
    print("Command executed successfully.")
else:
    print("Command failed with return code", return_code)