import random
import string

available_chars = [
    ch for ch in string.ascii_letters + string.digits
    if ch not in ('l', 'I', '1', 'o', 'O', '0')
]

def generate_password(m):
    while True:
        password = random.sample(available_chars, m)
        password_str = ''.join(password)
        if any(c.isdigit() for c in password_str) and \
           any(c.islower() for c in password_str) and \
           any(c.isupper() for c in password_str):
            return password_str


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        password = generate_password(m)
        passwords.add(password)
    return list(passwords)


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
