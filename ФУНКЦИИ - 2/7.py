def find_mountain(heightsMap):
    max_value = float('-inf')
    max_row, max_col = -1, -1

    for i in range(len(heightsMap)):
        for j in range(len(heightsMap[i])):
            if heightsMap[i][j] > max_value:
                max_value = heightsMap[i][j]
                max_row, max_col = i, j
    return max_row, max_col


a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
row, col = find_mountain(a)
print(row, col)  # Выведет (1, 2)

a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
row, col = find_mountain(a)
print(a[row][col])  # Выведет 4
