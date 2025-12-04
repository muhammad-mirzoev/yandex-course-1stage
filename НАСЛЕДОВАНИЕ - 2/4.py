class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(Triangle, a):
        Triangle.a = a
        Triangle.b = a
        Triangle.c = a

    def perimeter(self):
        return Triangle.perimeter(self)
