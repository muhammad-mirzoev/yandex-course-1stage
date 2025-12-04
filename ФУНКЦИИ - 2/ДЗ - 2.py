def possible_turns(cell):
    knight_moves = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]

    x = ord(cell[0]) - ord('A') + 1
    y = int(cell[1])

    possible_cells = []

    for dx, dy in knight_moves:
        new_x, new_y = x + dx, y + dy
        if 1 <= new_x <= 8 and 1 <= new_y <= 8:
            possible_cells.append(f"{chr(new_x + ord('A') - 1)}{new_y}")
    return sorted(possible_cells)


# Примеры использования:
print(possible_turns("B1"))  # ['A3', 'C3', 'D2']
print(possible_turns("H8"))  # ['F7', 'G6']
