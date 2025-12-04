time = input()

if time in ["5", "6", "7", "8", "9", "10"]:
    print("Утро")
elif time in ["11", "12", "13", "14", "15", "16", "17"]:
    print("День")
elif time in ["18", "19", "20", "21", "22"]:
    print("Вечер")
elif time in ["23", "0", "1", "2", "3", "4"]:
    print("Ночь")
else:
    print("Ошибка")