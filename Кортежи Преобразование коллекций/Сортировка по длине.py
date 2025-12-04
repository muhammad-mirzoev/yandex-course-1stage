n = int(input())

strings = [input().strip() for _ in range(n)]

for i in range(n):
    for j in range(n - 1 - i):
        if (len(strings[j]) > len(strings[j + 1]) or
                (len(strings[j]) == len(strings[j + 1]) and strings[j] > strings[j + 1])):
            strings[j], strings[j + 1] = strings[j + 1], strings[j]

for string in strings:
    print(string)
