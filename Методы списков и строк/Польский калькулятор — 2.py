import math


def process_operator(stack, operator):
    if operator == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif operator == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif operator == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif operator == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a // b)
    elif operator == '~':
        a = stack.pop()
        stack.append(-a)
    elif operator == '!':
        a = stack.pop()
        stack.append(math.factorial(a))
    elif operator == '#':
        a = stack.pop()
        stack.append(a)
        stack.append(a)
    elif operator == '@':
        c = stack.pop()
        b = stack.pop()
        a = stack.pop()
        stack.append(b)
        stack.append(c)
        stack.append(a)


def evaluate_rpn(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            process_operator(stack, token)

    return stack[0]


expression = input().strip()

print(evaluate_rpn(expression))
