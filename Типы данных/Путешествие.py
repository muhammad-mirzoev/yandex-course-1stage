city_july = input().strip()
city_august = input().strip()

if ((city_july == "Тула" or city_august == "Пенза") and city_july != city_august and not
        (city_july == "Тула" and city_august == "Пенза")):
    print("ДА")
else:
    print("НЕТ")