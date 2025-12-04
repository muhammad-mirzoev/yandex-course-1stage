passwd_lines = []
while True:
    line = input().strip()
    if line == "":
        break
    passwd_lines.append(line)

popular_passwords = input().strip().split(';')

for line in passwd_lines:
    fields = line.split(':')
    login = fields[0]
    password = fields[1]
    additional_info = fields[4]

    if password in popular_passwords:
        name = additional_info.split(',')[0]

        print(f"To: {login}")
        print(f"{name}, ваш пароль слишком простой, смените его.")
