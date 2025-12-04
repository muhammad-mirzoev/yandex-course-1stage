n = int(input())

for i in range(1, n + 1):
    line = input()
    index = line.find("кот")
    if index != -1:
        print(i, index + 1)
