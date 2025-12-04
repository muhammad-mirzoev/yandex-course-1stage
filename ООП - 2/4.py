import math

class Square:
    def __init__(self, side):
        self.side = side

    def extrude(self, h):
        return self.side ** 2 * h


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def extrude(self, h):
        return self.width * self.height * h


class Triangle:
    def __init__(self, side):
        self.side = side

    def extrude(self, h):
        area = (math.sqrt(3) / 4) * self.side ** 2
        return area * h


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def extrude(self, h):
        area = math.pi * self.radius ** 2
        return area * h


sq = Square(1)
rec = Rectangle(1, 2)
tr = Triangle(1)
cir = Circle(1)

for item in (sq, rec, tr, cir):
    print(item.extrude(1))
