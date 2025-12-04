name = float(input())
if (name % 4 == 0 and name % 100 != 0) or (name % 400 == 0):
    print("Високосный")
else:
    print("Не високосный")
