required_boards = int(input())
board_count = 0

while True:
    line = input().strip()

    if line == "КОНЕЦ":
        break

    if "доска" in line or "дощечка" in line:
        board_count += 1
        print(f"Прибили {board_count} дощечку.")

    if board_count == required_boards:
        print("ГОТОВО")
        break

if board_count < required_boards:
    print("МАЛОВАТО")
