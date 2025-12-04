size = int(input())

for row in range(size, 0, -1):
    for col in range(size):
        if col > 0:
            print(" ", end="")
        print(f"{chr(65 + col)}{row}", end="")
    print()
