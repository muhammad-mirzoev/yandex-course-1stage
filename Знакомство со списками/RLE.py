s = input().strip()

n = len(s)
count = 1
result = []

for i in range(1, n):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result.append(f"{count} {s[i - 1]}")
        count = 1
result.append(f"{count} {s[-1]}")

print("\n".join(result))
