import os
import subprocess
import platform
import sys

if len(sys.argv) < 2:
    print("Usage: python archk.py <folder_path>")
    sys.exit(1)

folder_path = sys.argv[1]

if not os.path.isdir(folder_path):
    print(f"{folder_path} is not a valid directory")
    sys.exit(1)

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        output = subprocess.check_output(["file", "-b", file_path])
        if "PE32+" in output.decode():
            print(f"\033[32m{file_path}: 64-bit\033[0m")
        elif "PE32" in output.decode():
            print(f"\033[31m{file_path}: 32-bit\033[0m")
        else:
            print(f"{file_path}: Unknown architecture")
