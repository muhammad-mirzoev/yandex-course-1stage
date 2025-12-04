class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        if abs(self.col - col) * abs(self.row - row) == 2 and self.row != row and self.col != col:
            return True
        return False


WHITE=1
BLACK=2

row0 = 2
col0 = 2
knight = Knight(row0, col0, WHITE)

print('white' if knight.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(knight.char(), end='')
        elif knight.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()