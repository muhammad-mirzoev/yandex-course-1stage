total = input().strip()
stack = []

tokens = total.split()

for token in tokens:
    if token in '+-*/':
        b = stack.pop()
        a = stack.pop()

        if token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)
    else:
        stack.append(int(token))

print(stack[0])
