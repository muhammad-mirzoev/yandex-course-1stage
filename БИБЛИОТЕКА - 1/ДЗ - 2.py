import random
import string


def generate_password(m):
    allowed_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    allowed_chars = allowed_chars.replace('l', '') \
        .replace('I', '') \
        .replace('1', '') \
        .replace('o', '') \
        .replace('O', '') \
        .replace('0', '')

    while True:
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits)
        ]

        password += random.choices(allowed_chars, k=m - 3)
        random.shuffle(password)
        password = ''.join(password)

        if (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password)):
            if not any(ch in password for ch in {'I', 'l', '1', 'o', 'O', '0'}):
                return password


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        password = generate_password(m)
        passwords.add(password)
    return list(passwords)
