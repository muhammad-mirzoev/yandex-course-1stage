r = int(input())

table = []
for _ in range(r):
    row = input().split(',')
    table.append(row)

n = int(input())

for _ in range(n):
    row_idx, col_idx = map(int, input().split(','))
    print(table[row_idx][col_idx])
