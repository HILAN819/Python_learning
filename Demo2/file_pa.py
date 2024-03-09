# from pathlib import Path

# file_path = Path("template.html").resolve()
# print(f"Absolute path to template.html: {file_path}")

# import sys
# print("Script name: ", sys.argv[0])
# print("command line arguments", sys.argv[1:])

import subprocess

# with open('output.txt', 'w', encoding="utf-8") as f:
#     p1 = subprocess.run(["ls", "-la"], stdout=f, text=True)
# print(p1.stdout)

# p1 = subprocess.run(["ls", "-la", "dne"],
#                     capture_output=True, text=True, check=True)
# print(p1.returncode)
# print(p1.stderr)

# p2 = subprocess.run(["ls", "-la", "dne"],
#                     stderr=subprocess.DEVNULL, text=True)

# print(p2.stderr)

p3 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True)
print(p3.stdout)

p4 = subprocess.run(['grep', '-n', 'file'],
                    capture_output=True, text=True, input=p3.stdout)
print(p4.stdout)
print(p4.stderr)
