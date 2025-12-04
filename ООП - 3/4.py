class Scrabble:
    letter_scores = {
        'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    def __init__(self, letters):
        self.letters = letters.upper()
        self.letter_count = {letter: self.letters.count(letter) for letter in set(self.letters)}
        self.total_points = sum(self.letter_scores[letter] * self.letter_count[letter] for letter in self.letter_count)
        self.total_letters = len(self.letters)

    def __str__(self):
        return f"Scrabble('{self.letters}')"

    def __call__(self, word):
        word = word.upper()
        word_count = {letter: word.count(letter) for letter in set(word)}
        for letter, count in word_count.items():
            if self.letter_count.get(letter, 0) < count:
                return 0
        return sum(self.letter_scores[letter] * word_count[letter] for letter in word_count)

    def __eq__(self, other):
        return (self.total_points, self.total_letters) == (other.total_points, other.total_letters)

    def __lt__(self, other):
        return (self.total_points, self.total_letters) < (other.total_points, other.total_letters)

    def __le__(self, other):
        return (self.total_points, self.total_letters) <= (other.total_points, other.total_letters)

    def __ne__(self, other):
        return (self.total_points, self.total_letters) != (other.total_points, other.total_letters)

    def __gt__(self, other):
        return (self.total_points, self.total_letters) > (other.total_points, other.total_letters)

    def __ge__(self, other):
        return (self.total_points, self.total_letters) >= (other.total_points, other.total_letters)


# Пример использования:
sc = Scrabble('SCRABBLE')
sc1 = Scrabble('ALLOWANCE')

print(sc('SCLERA'))  # 8
print(sc('CRABBY'))  # 0
print(sc1('NEWTON'))  # 0
print(sc1('CLOWN'))  # 10

# Сравнение экземпляров
print(sc('SCRABBLE'))  # 14
print(sc1('ALLOWANCE'))  # 14
print(sc > sc1, sc <= sc1, sc != sc1, sc >= sc1)  # False True True False
