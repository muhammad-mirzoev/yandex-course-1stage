n = int(input())
sequence = [int(input()) for _ in range(n)]

for i in range(n - 1):
    print(sequence[i] + sequence[i + 1])
