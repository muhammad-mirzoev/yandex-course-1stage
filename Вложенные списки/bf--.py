tape = [0] * 30000
pointer = 0

program = input().strip()

output = []

for command in program:
    if command == '>':
        pointer = (pointer + 1) % 30000
    elif command == '<':
        pointer = (pointer - 1) % 30000
    elif command == '+':
        tape[pointer] = (tape[pointer] + 1) % 256
    elif command == '-':
        tape[pointer] = (tape[pointer] - 1) % 256
    elif command == '.':
        output.append(tape[pointer])

for num in output:
    print(num)
