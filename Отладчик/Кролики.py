n = int(input())

a, b = 1, 1
number = 2

while b < n:
    a, b = b, a + b
    number += 1

if b == n:
    print(number)
else:
    print("НЕТ")
