def bracket_check(test_string):
    stack = []

    for char in test_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                print("NO")
                return
            stack.pop()

    if not stack:
        print("YES")
    else:
        print("NO")
