name = input()
index = int(input())

if 1 <= index <= len(name):
    print(name[index - 1])
else:
    print("ОШИБКА")
