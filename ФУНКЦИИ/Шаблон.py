def template(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        p = perimeter / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

        is_isosceles = (a == b or b == c or a == c)
        is_equilateral = (a == b == c)

        print(f"Периметр: {perimeter}")
        print(f"Площадь: {area}")
        print(f"Равнобедренный: {'да' if is_isosceles else 'нет'}")
        print(f"Равносторонний: {'да' if is_equilateral else 'нет'}")
    else:
        print(None)
