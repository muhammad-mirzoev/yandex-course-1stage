n = int(input())
board = [input().strip() for _ in range(n)]

winner = '-'

for row in board:
    for i in range(n - 2):
        if row[i] == row[i + 1] == row[i + 2] and row[i] != '.':
            winner = row[i]
            break
    if winner != '-':
        break

if winner == '-':
    for col in range(n):
        for i in range(n - 2):
            if board[i][col] == board[i + 1][col] == board[i + 2][col] and board[i][col] != '.':
                winner = board[i][col]
                break
        if winner != '-':
            break

print(winner)
