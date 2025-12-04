numbers = list(map(int, input().split()))
m, k = map(int, input().split())

result = sum(numbers[i]**2 for i in range(m, k + 1))

print(result)
