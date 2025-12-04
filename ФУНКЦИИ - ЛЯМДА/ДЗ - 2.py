input_string = input()
words = input_string.split()

max_len = max(len(word) for word in words)
result = map(lambda word: word.rjust(max_len, '*'), words)

for word in result:
    print(word)
