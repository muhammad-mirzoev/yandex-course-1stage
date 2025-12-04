logins = input().split(',')


def is_valid(login):
    for char in login:
        if not (char.isalnum() or char == '_'):
            return False
    return True


invalid_logins = [login for login in logins if not is_valid(login)]

if invalid_logins:
    invalid_logins.sort()

    max_length = max(len(login) for login in invalid_logins)

    for login in invalid_logins:
        print(login.rjust(max_length))
