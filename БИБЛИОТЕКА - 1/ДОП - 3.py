import random

n = int(input())

inside_circle = 0

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        inside_circle += 1

pi_approximation = 4 * inside_circle / n

print(pi_approximation)
