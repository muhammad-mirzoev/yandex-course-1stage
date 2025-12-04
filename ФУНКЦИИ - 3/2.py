def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def larger_root(p, q):
    D = discriminant(1, p, q)
    sqrt_D = D ** 0.5
    return (-p + sqrt_D) / 2


def smaller_root(p, q):
    D = discriminant(1, p, q)
    sqrt_D = D ** 0.5
    return (-p - sqrt_D) / 2


def main():
    p = float(input())
    q = float(input())

    D = discriminant(1, p, q)
    print(D)

    x1 = smaller_root(p, q)
    x2 = larger_root(p, q)

    print(f"{x1} {x2}")


print(smaller_root(2, 1))
print(larger_root(2, 1))
print(discriminant(1, 2, 1))
