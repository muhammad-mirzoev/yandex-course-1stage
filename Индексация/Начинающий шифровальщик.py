message = input().strip()

result = ""

for i, char in enumerate(message):
    code = ord(char)

    if i > 0:
        result += ", "
    result += str(code)

print(result)
