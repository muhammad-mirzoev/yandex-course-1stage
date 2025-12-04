class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        self.a = a
        self.b = b
        self.c = c


class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side, base):
        super().__init__(equal_side, equal_side, base)
        self.equal_side = equal_side
        self.base = base


class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side


class Quadrilateral(Polygon):
    def __init__(self, sides):
        super().__init__(sides)


class Parallelogram(Quadrilateral):
    def __init__(self, base, side, height):
        super().__init__([base, side, base, side])
        self.base = base
        self.side = side
        self.height = height


class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, height, height)
        self.width = width
        self.height = height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
