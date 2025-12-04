username = input()

for char in username:
    if not ('a' <= char <= 'z' or '0' <= char <= '9' or char == '_'):
        print(f"Неверный символ: {char}")
        break
else:
    print("OK")
