number = input().strip()

result = [number[i:len(number) - i] for i in range(len(number))]

for item in result:
    print(item)
