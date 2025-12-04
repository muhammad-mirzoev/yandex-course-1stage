text = input().strip().lower()

max_freq = 0
result_char = ''

for char in set(text):
    if char != ' ':
        freq = text.count(char)
        if freq > max_freq or (freq == max_freq and char < result_char):
            max_freq = freq
            result_char = char

print(result_char)
