class FlowingRectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.tg = a / b
        self.S = a * b / 2

    def __add__(self, other):
        self.S += other.S
        self.b = (2 * self.S / self.tg) ** 0.5
        self.a = (2 * self.S * self.tg) ** 0.5

    def __sub__(self, other):
        if other.S >= self.S:
            self.S, self.a, self.b = 0, 0, 0
        else:
            self.S -= other.S
            self.b = (2 * self.S / self.tg) ** 0.5
            self.a = (2 * self.S * self.tg) ** 0.5

    def get_width(self):
        return round(self.a, 2)

    def get_height(self):
        return round(self.b, 2)


# Пример
fr_1 = FlowingRectangle(12, 5)
fr_2 = FlowingRectangle(60, 1)
fr_1 + fr_2
print(fr_1.get_width(), fr_1.get_height())
fr_1 - fr_2
print(fr_1.get_width(), fr_1.get_height())