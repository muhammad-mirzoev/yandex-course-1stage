class NaturalNumber:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f'{self.__class__.__name__}({self.n})'

    def __add__(self, other):
        return NaturalNumber(self.n + other.n)

    def __sub__(self, other):
        res = self.n - other.n
        if res > 0:
            return NaturalNumber(res)
        return NaturalNumber(None)


class Integer(NaturalNumber):
    def __add__(self, other):
        return Integer(self.n + other.n)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Integer(self.n - other.n)

    def __rsub__(self, other):
        return Integer(other.n - self.n)


class RealNumber(Integer):
    def __add__(self, other):
        return RealNumber(self.n + other.n)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return RealNumber(self.n - other.n)

    def __rsub__(self, other):
        return RealNumber(other.n - self.n)


class ComplexNumber(RealNumber):
    def __add__(self, other):
        return ComplexNumber(self.n + other.n)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return ComplexNumber(self.n - other.n)

    def __rsub__(self, other):
        return ComplexNumber(other.n - self.n)