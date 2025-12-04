n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split(', ')))
    matrix.append(row)

sum_diag = 0

for i in range(n):

    matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]

    sum_diag += matrix[i][i]
    sum_diag += matrix[i][n - i - 1]

for row in matrix:
    print(' '.join(map(str, row)))

print(sum_diag)
