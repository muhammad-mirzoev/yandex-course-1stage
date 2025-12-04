n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

for i in range(n):
    for j in range(n - i - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

for num in numbers:
    print(num)
