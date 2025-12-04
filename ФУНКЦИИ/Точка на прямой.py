def line(s, t):
    if 'x' in s:
        k, b = s.split('x')
        k = float(k) if k not in ('', '+', '-') else float(k + '1')
        b = float(b) if b not in ('', '+', '-') else float(b + '1')
    else:
        k = 0
        b = float(s)

    x_t, y_t = map(float, t.split(';'))

    if k * x_t + b == y_t:
        print(True)
    else:
        print(False)


# Примеры
line("1x+6", "1;7")  # True
line("5x-10", "5;-9")  # False
line("0x+7", "3;7")  # True
line("3.5x+0", "2;7")  # True
