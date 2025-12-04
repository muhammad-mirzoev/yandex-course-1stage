n = int(input())
parts = [input() for _ in range(n)]

m = int(input())
for _ in range(m):
    print(parts[int(input()) - 1])
    