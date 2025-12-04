n = int(input())

strings = [input().strip() for _ in range(n)]

for i in range(n):
    for j in range(n - 1 - i):
        if strings[j] > strings[j + 1]:
            strings[j], strings[j + 1] = strings[j + 1], strings[j]

for string in strings:
    print(string)
