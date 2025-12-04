from sys import stdin as get


def num_code(char: str):
    char = char.upper()
    return ord(char) - ord("A") + 1


words = []
for w in get:
    words.append(w.lstrip().rstrip())

print(*sorted(words, key=lambda k: (sum([num_code(i) for i in k]), k)),
      sep="\n")
