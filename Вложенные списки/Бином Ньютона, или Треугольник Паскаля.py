n = int(input())

row = [1]

for _ in range(n):
    print(" ".join(map(str, row)))

    next_row = [1]
    for i in range(1, len(row)):
        next_row.append(row[i - 1] + row[i])
    next_row.append(1)
    row = next_row
