M = int(input())
N = int(input())

count = {}

for _ in range(M + N):
    name = input().strip()
    if name in count:
        count[name] += 1
    else:
        count[name] = 1

only_one_language = sum(1 for value in count.values() if value == 1)

if only_one_language > 0:
    print(only_one_language)
else:
    print("NO")