while True:
    number = int(input())

    if number == 0:
        break

    if number % 3 == 0 and number % 7 == 0:
        print("Караул!")
        break
    elif number % 3 == 0:
        print("несчастливое")
    elif number % 7 == 0:
        print("опасное")
    else:
        print(number)