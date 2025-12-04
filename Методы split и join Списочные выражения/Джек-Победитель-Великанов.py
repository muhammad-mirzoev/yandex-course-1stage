n = int(input())
titles = []

for _ in range(n):
    words = []
    while True:
        line = input().strip()
        if line == '*':
            break
        words.extend(line.split())
    titles.append('-'.join(words))

print(', '.join(reversed(titles)))
