def roots_of_quadratic_equation(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return ["all"]

    if a == 0:
        if b == 0:
            if c == 0:
                return ["all"]
            else:
                return []
        else:
            return [-c / b]

    D = b * b - 4 * a * c

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return [x1, x2]
    elif D == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return []
