def solve(*coefficients):
    n = len(coefficients)
    if n == 2:
        a, b = coefficients
        if a == 0:
            if b == 0:
                return "ANY"
            else:
                return []
        return [-b / a]
    elif n == 3:
        a, b, c = coefficients
        if a == 0:
            if b == 0:
                if c == 0:
                    return "ANY"
                else:
                    return []
            return [-c / b]
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return []
        elif discriminant == 0:
            return [-b / (2 * a)]
        else:
            sqrt_disc = discriminant ** 0.5
            x1 = (-b + sqrt_disc) / (2 * a)
            x2 = (-b - sqrt_disc) / (2 * a)
            return sorted([x1, x2])
    elif n == 1:
        c = coefficients[0]
        if c == 0:
            return "ANY"
        else:
            return []


def main():
    coefficients = list(map(float, input().split()))
    roots = solve(*coefficients)

    if roots == "ANY":
        print("-3 -2 -1 0 1 2 3")
    elif not roots:
        print()
    else:
        print(" ".join(map(str, roots)))


main()
