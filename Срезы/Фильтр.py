a = int(input())

for _ in range(a):
    line = input().strip()

    if line.startswith("####"):
        continue

    if line.startswith("%%"):
        line = line[2:]

    print(line)
