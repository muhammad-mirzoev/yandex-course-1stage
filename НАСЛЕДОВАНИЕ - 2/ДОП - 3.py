import math


class RegularPolygon:
    def __init__(self, sides=3):
        self.sides = sides

    def inner_corner(self):
        return round((self.sides - 2) * 180 / self.sides, 2)

    def __str__(self):
        return f"RegularPolygon, {self.inner_corner()} degree"


class Square(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(sides=4)
        self.side_length = side_length

    def area(self):
        return round(self.side_length ** 2, 2)

    def perimeter(self):
        return round(self.side_length * 4, 2)

    def __str__(self):
        return f"Square, {self.inner_corner()} degree, 4 sides"


class Triangle(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(sides=3)
        self.side_length = side_length

    def area(self):
        return round((math.sqrt(3) / 4) * (self.side_length ** 2), 2)

    def perimeter(self):
        return round(self.side_length * 3, 2)

    def __str__(self):
        return f"Triangle, {self.inner_corner()} degree, 3 sides"


class Hexagon(Triangle):
    def __init__(self, side_length):
        super().__init__(side_length)

    def circumcircle(self):
        return round(self.side_length / math.sqrt(3), 2)

    def __str__(self):
        return f"Hexagon, {self.inner_corner()} degree, 6 sides"


# Пример использования:
s = Square(10)
print(s)
print(s.area(), s.perimeter())

t = Triangle(10)
print(t)
print(t.area(), t.perimeter())

h = Hexagon(10000)
print(h)
print(h.area(), h.perimeter())
