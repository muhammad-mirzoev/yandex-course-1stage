import random
import string


def generate_password(m):
    allowed_chars = ''.join([c for c in string.ascii_letters + string.digits if c not in "lIoO01"])
    password = ''.join(random.sample(allowed_chars, m))
    return password


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        passwords.add(generate_password(m))

    return list(passwords)


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
