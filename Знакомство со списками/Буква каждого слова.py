n = int(input())
lines = [input() for _ in range(n)]
letter_number = int(input())

for line in lines:
    if len(line) >= letter_number:
        print(line[letter_number - 1], end="")
