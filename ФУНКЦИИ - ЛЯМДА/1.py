def arithmetic_operation(operation):
    if operation == '+':
        return lambda x, y: x + y
    elif operation == '-':
        return lambda x, y: x - y
    elif operation == '*':
        return lambda x, y: x * y
    elif operation == '/':
        return lambda x, y: x / y if y != 0 else ''
    else:
        raise ValueError


operation = arithmetic_operation('+')
print(operation(1, 4))
