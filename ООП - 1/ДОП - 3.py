class Robot:
    def __init__(self, position):
        x, y = position
        if not (0 <= x <= 100 and 0 <= y <= 100):
            raise ValueError()
        self.x = x
        self.y = y
        self._last_path = [(x, y)]

    def move(self, commands):
        self._last_path = [(self.x, self.y)]
        for command in commands:
            if command == 'N' and self.y < 100:
                self.y += 1
            elif command == 'S' and self.y > 0:
                self.y -= 1
            elif command == 'E' and self.x < 100:
                self.x += 1
            elif command == 'W' and self.x > 0:
                self.x -= 1
            self._last_path.append((self.x, self.y))
        return (self.x, self.y)

    def path(self):
        return self._last_path



r = Robot((0, 0))
print(r.move('NENW'))
print(*r.path())