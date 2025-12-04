result = []

while True:
    word = input().strip()

    if word == "":
        break

    letter_counts = {}
    frequencies = []

    for letter in word:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    for letter in word:
        frequencies.append(letter_counts[letter])

    result.append(frequencies)

print(result)
