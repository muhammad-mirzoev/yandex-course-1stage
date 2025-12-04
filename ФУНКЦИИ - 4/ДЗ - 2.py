def transpose(matrix):
    matrix[:] = [list(row) for row in zip(*matrix)]


matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)
matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)