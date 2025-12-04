shift = int(input())
message = input()

encrypted_message = ""

for char in message:
    if 'А' <= char <= 'Я':
        encrypted_char = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
        encrypted_message += encrypted_char
    elif 'а' <= char <= 'я':
        encrypted_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
        encrypted_message += encrypted_char
    else:
        encrypted_message += char

print(encrypted_message)
