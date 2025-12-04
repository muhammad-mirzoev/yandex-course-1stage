class Wardrobe:
    def __init__(self, *things):
        self.things = things

    def _volume(self):
        return 0, len(self.things)

    def __str__(self):
        return ' '.join(self.things)

    def __lt__(self, other):
        return self._volume() < other._volume()

    def __eq__(self, other):
        return self._volume() == other._volume()

    def __le__(self, other):
        return self._volume() <= other._volume()


class JustWardrobe(Wardrobe):
    def __init__(self, *things):
        super().__init__(*things)

    def __str__(self):
        return (', '.join(self.things) + '.').capitalize()


class MagicWardrobe(Wardrobe):
    def __init__(self, *things):
        super().__init__(*things)

    def __str__(self):
        return (', '.join(sorted(self.things)) + '.').title()

    def _volume(self):
        return 1, len(self.things)



# Пример 1
wa = Wardrobe("socks", "jacket", "hat")
jw = JustWardrobe("trousers", "blouse")
mw = MagicWardrobe("Narnia", "Wonderland", "Dreamland")
print(*[wa, jw, mw], sep='\n')

# Пример 2
jw1 = JustWardrobe("socks", "jacket", "hat")
jw2 = JustWardrobe("trousers", "blouse")
mw1 = MagicWardrobe("Narnia", "Wonderland", "Dreamland")
mw2 = MagicWardrobe("Kingdom", "Mordor", "Middle Earth")
print(jw1 > jw2)
print(jw1 == mw1)
print(jw2 <= mw2)
print(mw1 != mw2)
