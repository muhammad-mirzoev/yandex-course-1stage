def allocation(data):
    not_booked = []

    for row, seat in data:
        row_index = row - 1
        seat_index = seat - 1

        if places[row_index][seat_index] == 1:
            not_booked.append((row, seat))
        else:
            places[row_index][seat_index] = 1
    return not_booked


places = [[1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]
data = [(2, 3), (1, 4), (3, 1), (2, 3), (3, 3)]
print(allocation(data))  # [(2, 3), (3, 3)]
