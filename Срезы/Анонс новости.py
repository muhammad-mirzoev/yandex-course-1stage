max_length = int(input())
n = int(input())

for _ in range(n):
    title = input().strip()

    if len(title) > max_length:
        title = title[:max_length - 3] + "..."
    print(title)
