def horse2(position):
    column_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    reverse_column_map = {v: k for k, v in column_map.items()}

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    column = column_map[position[0]]
    row = int(position[1])

    result = []

    for move in moves:
        new_column = column + move[0]
        new_row = row + move[1]
        if 1 <= new_column <= 8 and 1 <= new_row <= 8:
            result.append(reverse_column_map[new_column] + str(new_row))

    for res in result:
        print(res)
