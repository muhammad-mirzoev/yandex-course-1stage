rows = int(input())
cols = int(input())

table = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(input())
    table.append(row)

for row in table:
    print("\t".join(row))

#вторая часть
print()

transposed_table = zip(*table)

for row in transposed_table:
    print("\t".join(row))
