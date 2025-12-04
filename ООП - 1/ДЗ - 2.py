class Rainbow:
    colors = ['red', 'orange', 'yellow', 'green', 'light blue', 'blue', 'violet']

    def __init__(self, rainbow_type=1):
        self.rainbow_type = rainbow_type

    def next_color(self, color):
        index = Rainbow.colors.index(color)

        if self.rainbow_type == 1 or self.rainbow_type == 3:
            return Rainbow.colors[(index + 1) % len(Rainbow.colors)]
        elif self.rainbow_type == 2:
            return Rainbow.colors[(index - 1) % len(Rainbow.colors)]


# Пример использования
rb1 = Rainbow(1)
print(rb1.next_color('violet'))  # Должен вывести 'red'

rb2 = Rainbow(2)
print(rb2.next_color('red'))  # Должен вывести 'violet'
