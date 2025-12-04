word = input()
step = int(input())

while len(word) > step:
    print(word[-step:])
    word = word[:-step]

    if len(word) <= step:
        break

    print(word[:step])
    word = word[step:]

if len(word) > 0:
    print(word)
