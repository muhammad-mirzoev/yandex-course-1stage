def circle_length(radius):
    pi = 3.14159
    return 2 * pi * radius


def circle_area(radius):
    pi = 3.14159
    return pi * radius * radius


def main():
    radius = float(input())
    length = circle_length(radius)
    area = circle_area(radius)
    print(f"{length} {area}")


print(circle_length(5))
print(circle_area(10))
main()