n_line = int(input())

for i in range(1, n_line + 1):
    for d in range(1, n_line + 1):
        print(i * d, end="\t")

    print()
