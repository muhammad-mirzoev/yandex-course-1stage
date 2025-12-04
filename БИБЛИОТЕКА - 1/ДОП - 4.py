import math


def multiplier(*args, key):
    filtered_numbers = [x for x in args if key(x)]
    if filtered_numbers:
        return math.prod(filtered_numbers)
    return None


print(multiplier(2, 3, 4, 5, key=lambda x: x % 2))
