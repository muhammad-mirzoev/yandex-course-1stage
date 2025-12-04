n = int(input())

for i in range(1, n + 1):
    line = input()
    pos = line.find("кот")

    if pos != -1:
        print(i, pos + 1)
