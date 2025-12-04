import sys

for idx, line in enumerate(sys.stdin, start=1):
    line = line.strip()
    if line.startswith("#"):
        comment = line[1:].strip()
        print(f"Line {idx}: {comment}")
