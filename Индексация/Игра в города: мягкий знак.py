word1 = input().strip()
word2 = input().strip()

if word1[-1] == 'ь':
    if word1[-2] == word2[0]:
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")
else:
    if word1[-1] == word2[0]:
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")
