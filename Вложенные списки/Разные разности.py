n = int(input())
numbers = [int(input()) for _ in range(n)]

differences = set()

for i in range(n):
    for j in range(n):
        differences.add(numbers[i] - numbers[j])

for diff in sorted(differences):
    print(diff)
