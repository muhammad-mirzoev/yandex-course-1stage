def equation(a, b):
    x1, y1 = map(float, a.split(';'))
    x2, y2 = map(float, b.split(';'))

    if x1 == x2:
        print(f"{x1}")
    elif y1 == y2:
        print(f"{y1}")
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        print(f"{k} {b}")
