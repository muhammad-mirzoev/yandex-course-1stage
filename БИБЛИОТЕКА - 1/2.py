import math


number = float(input())

if (number * 1000) % 10 >= 5:
    print(math.ceil(number * 100) / 100)
else:
    print(round(number, 2))