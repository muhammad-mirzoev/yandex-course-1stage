message = input().strip()
fav_number = int(input().strip())
fav_letter = input().strip()

if len(fav_letter) != 1:
    print("ОШИБКА")
else:
    if fav_number < 1 or fav_number > len(message):
        print("ОШИБКА")
    else:
        if message[fav_number - 1] == fav_letter:
            print("ДА")
        else:
            print("НЕТ")
