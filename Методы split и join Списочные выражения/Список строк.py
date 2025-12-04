input_string = input()
words = input_string.split()

formatted_output = f'[{", ".join([f"\"{word}\"" for word in words])}]'

print(formatted_output)
