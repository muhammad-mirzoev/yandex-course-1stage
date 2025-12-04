n = int(input())
numbers = [int(input()) for _ in range(n)]
total_sum = sum(numbers)

parity = total_sum % 2

remaining = [num for num in numbers if num % 2 == parity]
removed_sum = sum(num for num in numbers if num % 2 != parity)

print(removed_sum, remaining)
