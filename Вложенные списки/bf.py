program = input().strip()

memory = [0] * 30000
pointer = 0
program_counter = 0
program_length = len(program)

while program_counter < program_length:
    command = program[program_counter]

    if command == '+':
        memory[pointer] = (memory[pointer] + 1) % 256
    elif command == '-':
        memory[pointer] = (memory[pointer] - 1) % 256
    elif command == '>':
        pointer += 1
    elif command == '<':
        pointer -= 1
    elif command == '.':
        output = memory[pointer]
        print(output)
    elif command == '[':
        if memory[pointer] == 0:
            open_bracket_count = 1
            while open_bracket_count > 0:
                program_counter += 1
                if program[program_counter] == '[':
                    open_bracket_count += 1
                elif program[program_counter] == ']':
                    open_bracket_count -= 1
    elif command == ']':
        if memory[pointer] != 0:
            close_bracket_count = 1
            while close_bracket_count > 0:
                program_counter -= 1
                if program[program_counter] == ']':
                    close_bracket_count += 1
                elif program[program_counter] == '[':
                    close_bracket_count -= 1

    program_counter += 1
