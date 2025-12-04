class Seat:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}({self.size}, {self.color})"


class Chair(Seat):
    def __init__(self, size, color, height, num_legs):
        super().__init__(size, color)
        self.height = height
        self.num_legs = num_legs

    def __str__(self):
        return f"{self.__class__.__name__}({self.size}, {self.color}, {self.height}, {self.num_legs})"


class ArmChair(Seat):
    def __init__(self, size, color, height, material):
        super().__init__(size, color)
        self.height = height
        self.material = material

    def __str__(self):
        return f"{self.__class__.__name__}({self.size}, {self.color}, {self.height}, {self.material})"


class Stool(Seat):
    def __init__(self, size, color, num_legs):
        super().__init__(size, color)
        self.num_legs = num_legs

    def __str__(self):
        return f"{self.__class__.__name__}({self.size}, {self.color}, {self.num_legs})"


class BagChair(Seat):
    def __init__(self, size, color, material):
        super().__init__(size, color)
        self.material = material

    def __str__(self):
        return f"{self.__class__.__name__}({self.size}, {self.color}, {self.material})"


# Пример
se = Seat(35, "beige")
ch = Chair(40, "pink", 80, 3)
ach = ArmChair(70, "black", 85, "leather")
st = Stool(48, "white", 3)
bc = BagChair(75, "orange", "matting")

for item in se, ch, ach, st, bc:
    print(item)
