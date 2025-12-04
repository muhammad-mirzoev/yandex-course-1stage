class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum(self.transform(n) for n in range(1, N + 1))


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)


# Пример использования
square_summator = SquareSummator()
print(square_summator.sum(3))  # Сумма квадратов чисел от 1 до 3 -> 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

cube_summator = CubeSummator()
print(cube_summator.sum(3))  # Сумма кубов чисел от 1 до 3 -> 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36

power_summator = PowerSummator(4)  # Пример с произвольной степенью
print(power_summator.sum(3))  # Сумма чисел от 1 до 3 в степени 4 -> 1^4 + 2^4 + 3^4 = 1 + 16 + 81 = 98