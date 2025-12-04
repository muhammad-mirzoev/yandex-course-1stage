import random
import string


def generate_password(m):
    available_chars = string.ascii_letters + string.digits
    exclude_chars = "lIo01oO"
    available_chars = ''.join(c for c in available_chars if c not in exclude_chars)

    password = ''.join(random.choice(available_chars) for _ in range(m))
    return password


def main(n, m):
    passwords = set()

    while len(passwords) < n:
        passwords.add(generate_password(m))

    return list(passwords)


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
