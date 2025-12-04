class PearsBasket:
    def __init__(self, k):
        self.k = k

    def __floordiv__(self, other):
        if self.k % other:
            return [PearsBasket(self.k // other) for _ in range(other)] + [PearsBasket(self.k % other)]
        else:
            return [PearsBasket(self.k // other) for _ in range(other)]

    def __mod__(self, other):
        return self.k % other

    def __add__(self, other):
        return PearsBasket(self.k + other.k)

    def __sub__(self, other):
        if self.k < other:
            self.k = 0
        else:
            self.k = self.k - other
        return self

    def __str__(self):
        return str(self.k)

    def __repr__(self):
        return f'PearsBasket({self.k})'


# Пример использования
pb = PearsBasket(17)
array = pb // 4
print(array)  # [PearsBasket(4), PearsBasket(4), PearsBasket(4), PearsBasket(4), PearsBasket(1)]

pb_2 = PearsBasket(13)
pb_3 = pb + pb_2
print(pb_3)  # PearsBasket(30)

print(pb_3 % 7)  # 2

pb - 2
print([pb])  # [PearsBasket(15)]
