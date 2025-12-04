def quarters(*points):
    counts = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}

    for x, y in points:
        if x == 0 or y == 0:
            continue

        if x > 0 and y > 0:
            counts['I'] += 1
        elif x < 0 and y > 0:
            counts['II'] += 1
        elif x < 0 and y < 0:
            counts['III'] += 1
        elif x > 0 and y < 0:
            counts['IV'] += 1
    return counts


data = [(1, 1), (-1, 2), (-3, -1)]
for k, v in sorted(quarters(*data).items()):
    print(f'{k}:\t{v}')