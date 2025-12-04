N = int(input())
numbers = [int(input()) for _ in range(N)]

p = int(input())
q = int(input())

print(sum(numbers[p - 1:q]))