s = input().strip()

filtered_str = ''
for char in s:
    if char != ' ':
        filtered_str += char

is_palindrome = True
length = len(filtered_str)

for i in range(length // 2):
    if filtered_str[i] != filtered_str[length - i - 1]:
        is_palindrome = False
        break

print(is_palindrome)
