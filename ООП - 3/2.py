class ChairLeg:
    def __init__(self, length):
        self.length = length

    def __mul__(self, other):
        self.length *= other
        return self

    def __rmul__(self, other):
        self.length *= other
        return self

    def __floordiv__(self, other):
        self.length //= other
        return self

    def __mod__(self, other):
        return self.length % other

# Пример использования
chl = ChairLeg(15)
chl * 3
print(chl.length)
2 * chl
print(chl.length)
print(chl % 7)