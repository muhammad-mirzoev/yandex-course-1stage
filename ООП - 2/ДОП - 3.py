class LettersRhombus:
    def __init__(self, letter, filler=" "):
        self.letter = letter
        self.filler = filler
        self.size = ord(letter) - ord('A') + 1

    def rows(self):
        rows = []
        for i in range(self.size):
            row = [self.filler] * (2 * self.size - 1)
            row[self.size - 1 - i] = chr(ord('A') + i)
            row[self.size - 1 + i] = chr(ord('A') + i)
            rows.append(''.join(row))
        return rows + rows[-2::-1]

    def cols(self):
        rows = self.rows()
        cols = [''.join(row[i] for row in rows) for i in range(len(rows[0]))]
        return cols


# Пример 1
lines = LettersRhombus("D", "-")
print(*lines.rows(), sep="\n")

# Пример 2
lines = LettersRhombus("C")
print(*lines.cols(), sep="\n")
