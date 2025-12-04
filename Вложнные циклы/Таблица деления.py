m = int(input())
n = int(input())

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j == m:
            print(f"{j / i:.10f}")
        else:
            print(f"{j / i:.10f}", end=" ")