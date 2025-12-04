class BoundingRectangle:
    def __init__(self):
        self.left = float('inf')
        self.right = float('-inf')
        self.top = float('-inf')
        self.bottom = float('inf')

    def add_point(self, x, y):
        if x < self.left:
            self.left = x
        if x > self.right:
            self.right = x
        if y < self.bottom:
            self.bottom = y
        if y > self.top:
            self.top = y

    def width(self):
        return self.right - self.left

    def height(self):
        return self.top - self.bottom

    def bottom_y(self):
        return self.bottom

    def top_y(self):
        return self.top

    def left_x(self):
        return self.left

    def right_x(self):
        return self.right


rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print()