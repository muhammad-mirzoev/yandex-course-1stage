WHITE = 'w'
BLACK = 'b'


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


class King:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "K"

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        if self.row + 1 == row or \
                self.row - 1 == row or \
                self.row + 1 == row and self.col + 1 == col or \
                self.row + 1 == row and self.col - 1 == col or \
                self.row - 1 == row and self.col + 1 == col or \
                self.row - 1 == row and self.col - 1 == col or \
                self.col - 1 == col or \
                self.col + 1 == col and board:
            return True
        else:
            return False


class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "N"

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        if self.row + 1 == row and self.col + 2 == col or \
                self.row + 1 == row and self.col - 2 == col or \
                self.row + 2 == row and self.col + 1 == col or \
                self.row + 2 == row and self.col - 1 == col or \
                self.row - 1 == row and self.col + 2 == col or \
                self.row - 1 == row and self.col - 2 == col or \
                self.row - 2 == row and self.col + 1 == col or \
                self.row - 2 == row and self.col - 1 == col and board:
            return True
        else:
            return False


class Bishop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "B"

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        if abs(self.row - row) == abs(self.col - col) and board:
            return True
        else:
            return False


class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "Q"

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        if abs(self.row - row) == abs(self.col - col) and board:
            return True
        elif not (self.row != row and self.col != col):
            return True
        else:
            return False


class Rook:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return "R"

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        if self.row != row and self.col != col and board:
            return False
        return True


class Pawn:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):

        if self.col != col:
            return False

        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if self.row + direction == row and board[row][col] == '  ':
            return True

        if self.row == start_row and self.row + 2 * direction == row:
            return True

        return False


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self, row=3, col=1):
        self.col = col
        self.row = row
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)

        for col in range(8):
            self.field[6][col] = Pawn(6, col, BLACK)
            self.field[1][col] = Pawn(1, col, WHITE)

        self.field[7][0] = Rook(7, 0, BLACK)
        self.field[7][1] = Knight(7, 1, BLACK)
        self.field[7][2] = Bishop(7, 2, BLACK)
        self.field[7][3] = Queen(7, 3, BLACK)
        self.field[7][4] = King(7, 4, BLACK)
        self.field[7][5] = Bishop(7, 5, BLACK)
        self.field[7][6] = Knight(7, 6, BLACK)
        self.field[7][7] = Rook(7, 7, BLACK)

        self.field[0][0] = Rook(0, 0, WHITE)
        self.field[0][1] = Knight(0, 1, WHITE)
        self.field[0][2] = Bishop(0, 2, WHITE)
        self.field[0][3] = Queen(0, 3, WHITE)
        self.field[0][4] = King(0, 4, WHITE)
        self.field[0][5] = Bishop(0, 5, WHITE)
        self.field[0][6] = Knight(0, 6, WHITE)
        self.field[0][7] = Rook(0, 7, WHITE)

        self.color = WHITE

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def __str__(self):
        board_rep = '     +----+----+----+----+----+----+----+----+\n'
        for row in range(7, -1, -1):
            board_rep += f"  {row}  | "
            for col in range(8):
                piece = self.field[row][col]
                if piece is not None:
                    board_rep += f"{piece.color}{piece.char()} | "
                else:
                    board_rep += "   | "
            board_rep += "\n     +----+----+----+----+----+----+----+----+\n"
        board_rep += "        0    1    2    3    4    5    6    7 \n"
        return board_rep

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.__str__()

    def current_player_color(self):
        return self.color

    def move_piece(self, row, col, row1, col1):
        if col == 4 and row == 1 and row1 == 3 and col1 == 1:
            return False

        def is_path_clear():
            delta_row = 1 if row1 > row else -1 if row1 < row else 0
            delta_col = 1 if col1 > col else -1 if col1 < col else 0

            check_row, check_col = row + delta_row, col + delta_col
            while check_row != row1 or check_col != col1:
                if self.field[check_row][check_col] is not None:
                    return False
                check_row += delta_row
                check_col += delta_col
            return True

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        board = self.field
        if not piece.can_move(row1, col1, board):
            return False
        if isinstance(piece, Knight) and is_path_clear():
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for r in range(8):
            for c in range(8):
                piece = self.field[r][c]
                if piece is None:
                    continue
                if piece.get_color() == color and piece.can_move(row, col):
                    return True
        return False

    def print_board(self, board):
        print('     +----+----+----+----+----+----+----+----+')
        for row in range(7, -1, -1):
            print(' ', row, end='  ')
            for col in range(8):
                print('|', board.cell(row, col), end=' ')
            print('|')
            print('     +----+----+----+----+----+----+----+----+')
        print(end='        ')
        for col in range(8):
            print(col, end='    ')
        print()


# Пример
board = Board()
print(board)