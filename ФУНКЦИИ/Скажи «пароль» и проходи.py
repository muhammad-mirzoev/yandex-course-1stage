def ask_password():
    correct_password = "password"
    attempts = 3

    for _ in range(attempts):
        try:
            user_input = input()
            if user_input == correct_password:
                print("Пароль принят")
                return
        except EOFError:
            continue
    print("В доступе отказано")
