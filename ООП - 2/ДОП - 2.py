class Knight:
    def __init__(self, name, *weapons):
        self.name = name
        self.weapons = weapons

    def fight(self, weapon):
        consonants = ''.join([char for char in weapon if char not in 'aoeiuy'])
        if weapon in self.weapons:
            return consonants.upper()
        return None

    def info(self):
        return f"Knight({self.name})"

    def announce(self, lady):
        return f"Long live the noblest {lady}!"


class Squire:
    def __init__(self, name, knight_name, *weapons):
        self.name = name
        self.knight_name = knight_name
        self.weapons = weapons

    def fight(self, weapon):
        consonants = ''.join([char for char in weapon if char not in 'aoeiuy'])
        if weapon in self.weapons:
            return consonants.lower()
        return None

    def info(self):
        return f"Squire({self.name})"

    def praise(self):
        return f"Glory to {self.knight_name}!"


kn = Knight("Lancelot", "sword", "spear", "mace", "dirk")
sq = Squire("Jhonny", "Lancelot", "stick")

for item in (kn, sq):
    print(item.info())
    print(item.fight("sword"))
    print(item.fight("stick"))
    if isinstance(item, Knight):
        print(item.announce("Izabella"))
    else:
        print(item.praise())
