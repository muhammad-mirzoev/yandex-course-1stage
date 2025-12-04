def tic_tac_toe(field):
    for row in field:
        if row[0] == row[1] == row[2] and row[0] != '-':
            print(f"{row[0]} win")
            return

    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] and field[0][col] != '-':
            print(f"{field[0][col]} win")
            return

    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != '-':
        print(f"{field[0][0]} win")
        return
    if field[0][2] == field[1][1] == field[2][0] and field[0][2] != '-':
        print(f"{field[0][2]} win")
        return

    print("draw")


# Пример использования
data = """0 - 0
x x x
0 0 -"""
field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)
