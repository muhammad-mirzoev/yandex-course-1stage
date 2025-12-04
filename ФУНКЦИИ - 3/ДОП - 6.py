from math import sin, cos, radians, sqrt


def collect_stones():
    global ALPHA, L
    g = 9.8
    alpha_rad = radians(ALPHA)
    v = sqrt(L * g / sin(2 * alpha_rad))
    L -= 0.5
    return v


# Пример использования
ALPHA = 45
L = 10
print(collect_stones())  # первый бросок
print(collect_stones())  # второй бросок
print(collect_stones())  # третий бросок
