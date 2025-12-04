import random

n = int(input())
m = int(input())
k = int(input())

first_part = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
second_part = random.choice(range(n, m+1, k))
third_part = round(random.uniform(1, 9), 3)

serial_number = f"{first_part}-{second_part}-{third_part:.3f}"
print(serial_number)
