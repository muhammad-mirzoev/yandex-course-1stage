numbers = list(map(int, input().split()))
m, k = map(int, input().split())

result = sum(numbers[m:k + 1])

print(result)
