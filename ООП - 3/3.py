class Potato:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Potato({self.size})"

    def __truediv__(self, number):
        new_potato = Potato(self.size / number)
        self.size -= new_potato.size
        return new_potato

    def __itruediv__(self, number):
        self.size /= number
        return self


# Пример использования
pt = pt1 = Potato(7)
pt /= 4
print(pt)  # Вывод: Potato(1.75)
pt2 = pt / 3
print(pt, pt1, pt2, sep='\n')  # Вывод: Potato(1.1666666666666665), Potato(1.
