def golden_ratio(i):
    a, b = 1, 1
    for _ in range(i - 1):
        a, b = b, a + b
    print(b / a)
