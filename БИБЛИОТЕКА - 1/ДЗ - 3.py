import math


n = int(input())

max_distance = 0
for i in range(n):
    x = float(input())
    y = float(input())
    distance = math.sqrt(x**2 + y**2)
    if distance > max_distance:
        max_distance = distance

print(f"{max_distance:.3f}")
