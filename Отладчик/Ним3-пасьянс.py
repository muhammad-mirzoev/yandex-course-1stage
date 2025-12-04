a = int(input())
b = int(input())
c = int(input())

while True:
    pile = int(input())
    stones = int(input())

    if pile == 1:
        a -= stones
    elif pile == 2:
        b -= stones
    elif pile == 3:
        c -= stones

    print(a, b, c)

    if a == 0 and b == 0 and c == 0:
        break
