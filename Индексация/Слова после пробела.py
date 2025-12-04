string = input()

word = ""

for i in string:
    if i == " ":
        if word:
            print(word)
            word = ""
    else:
        word += i

if word:
    print(word)
