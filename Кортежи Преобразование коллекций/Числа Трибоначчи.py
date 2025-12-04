n = int(input())

a, b, c = 1, 1, 1

if n == 1:
    print(a)
elif n == 2:
    print(a, b)
elif n == 3:
    print(a, b, c)
else:
    print(a, b, c, end=" ")

    for _ in range(4, n + 1):
        next_num = a + b + c
        print(next_num, end=" ")
        a, b, c = b, c, next_num
