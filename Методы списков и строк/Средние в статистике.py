numbers = list(map(float, input().split()))
mean = sum(numbers) / len(numbers)

numbers.sort()

n = len(numbers)
if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print(f"{mean:.5f} {median:.5f}")
