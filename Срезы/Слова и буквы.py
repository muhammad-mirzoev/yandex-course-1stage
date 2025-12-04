shortest_word = None
longest_word = None

while True:
    word = input().strip()
    if word == "стоп":
        break

    if shortest_word is None or len(word) < len(shortest_word):
        shortest_word = word
    if longest_word is None or len(word) > len(longest_word):
        longest_word = word

for char in shortest_word:
    if char not in longest_word:
        print("НЕТ")
        break
else:
    print("ДА")
