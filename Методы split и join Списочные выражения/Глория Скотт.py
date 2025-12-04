input_str = input().strip()

words = input_str.split()
result = ' '.join(words[i] for i in range(2, len(words), 3))

print(result)
