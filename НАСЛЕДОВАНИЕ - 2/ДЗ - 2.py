class Fish:
    def swim(self):
        return "swim"

    def dive(self):
        return "dive"

    def breathe_with_gills(self):
        return "breathe_with_gills"


class LandAnimal:
    def walk_on_land(self):
        return "walk_on_land"

    def breathe_air(self):
        return "breathe_air"

    def feed_cubs(self):
        return "feed_cubs"


class Whale(Fish, LandAnimal):
    def filter_food(self, array, hole_size):
        return [food for food in array if food <= hole_size]

    def swim(self):
        return "swim"

    def dive(self):
        return "dive"

    def breathe_with_gills(self):
        return None

    def walk_on_land(self):
        return None

    def breathe_air(self):
        return "breathe_air"

    def feed_cubs(self):
        return None


# Пример 1
fish = Fish()
print(fish.breathe_with_gills())

bear = LandAnimal()
print(bear.walk_on_land())

whale = Whale()
print(whale.breathe_air())

# Пример 2
whale = Whale()
print(whale.breathe_with_gills())
array = [8, 21, 15, 3, 42, 17]
print(whale.filter_food(array, 15))
print(whale.dive())

# Пример 3
fish = Fish()
print(fish.swim())
bear = LandAnimal()
print(bear.breathe_air())
whale = Whale()
print(whale.swim())
array = [10, 5, 16, 9, 18, 22]
print(whale.filter_food(array, 17))
print(whale.dive())