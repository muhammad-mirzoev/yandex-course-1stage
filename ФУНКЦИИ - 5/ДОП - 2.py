def solve(*coefficients):
    n = len(coefficients)
    if n == 0 or n > 3:
        return None
    if n == 3:
        a, b, c = coefficients
        if a == 0:
            if b == 0:
                if c == 0:
                    return ["all"]
                else:
                    return []
            else:
                return [-c / b]
        else:
            D = b ** 2 - 4 * a * c
            if D < 0:
                return []
            elif D == 0:
                return [-b / (2 * a)]
            else:
                sqrt_D = D ** 0.5
                return sorted([(-b - sqrt_D) / (2 * a), (-b + sqrt_D) / (2 * a)])
    elif n == 2:
        b, c = coefficients
        if b == 0:
            if c == 0:
                return ["all"]
            else:
                return []
        else:
            return [-c / b]
    elif n == 1:
        c = coefficients[0]
        if c == 0:
            return ["all"]
        else:
            return []


print(sorted(solve(1, 2, 1)))
print(sorted(solve(1, -3, 2)))
