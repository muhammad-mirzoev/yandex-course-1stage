word1 = input()

while True:
    total = input()
    if word1[-1] != total[0]:
        print(total)
        break

    word1 = total
