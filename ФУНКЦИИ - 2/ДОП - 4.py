def brackets(line):
    stack = []

    for char in line:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


# Примеры:
line1 = "25 * (6 - 3 * (12 + 5)) - 2 * (3 + 14 / (15-9))"
print(brackets(line1))  # True

line2 = "12 / (9 + 2(5(3 - 14))"
print(brackets(line2))  # False
