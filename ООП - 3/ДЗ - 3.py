def equally(self, other):
    return self.wins == other.wins and len(self.weapons) == len(other.weapons) and len(self.name) == len(other.name)


def more(self, other):
    return True if (self.wins > other.wins) or (self.wins == other.wins and len(self.weapons) > len(other.weapons)) or (
            self.wins == other.wins and len(self.weapons) == len(other.weapons) and len(self.name) < len(
        other.name)) else False


def less(self, other):
    return True if (self.wins < other.wins) or (self.wins == other.wins and len(self.weapons) < len(other.weapons)) or (
            self.wins == other.wins and len(self.weapons) == len(other.weapons) and len(self.name) > len(
        other.name)) else False


class EpicHero:
    def __init__(self, name, wins, weapons):
        self.name = name
        self.wins = wins
        self.weapons = weapons

    def add_win(self):
        self.wins += 1

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def del_weapon(self, weapon):
        if weapon in self.weapons:
            self.weapons.remove(weapon)

    def __str__(self):
        return f'Epic Hero {self.name}, {self.wins}'

    def __repr__(self):
        return f"EpicHero('{self.name}', {self.wins}, {sorted(self.weapons)})"

    def __eq__(self, other):
        return equally(self, other)

    def __ne__(self, other):
        return not equally(self, other)

    def __gt__(self, other):
        return more(self, other)

    def __lt__(self, other):
        return less(self, other)

    def __le__(self, other):
        return less(self, other) or equally(self, other)

    def __ge__(self, other):
        return more(self, other) or equally(self, other)



eh_1 = EpicHero('Ilya', 2, ['mace', 'bow'])
eh_2 = EpicHero('Dobrynya', 2, ['knife'])
print(eh_1, eh_2, sep='\n')
print([eh_1, eh_2])
eh_2.add_weapon('sword')
print(eh_1 >= eh_2)