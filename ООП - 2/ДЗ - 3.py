class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, other):
        x_inter = max(self.x, other.x)
        y_inter = max(self.y, other.y)
        w_inter = min(self.x + self.w, other.x + other.w) - x_inter
        h_inter = min(self.y + self.h, other.y + other.h) - y_inter
        if w_inter > 0 and h_inter > 0:
            return Rectangle(x_inter, y_inter, w_inter, h_inter)
        else:
            return None

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h


rect1 = Rectangle(3, 5, 2, 1)
rect2 = Rectangle(1, 2, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())