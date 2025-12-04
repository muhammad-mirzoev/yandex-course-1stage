name11 = input()
name22 = input()
if ((name11 == "ДА" and name22 == "ДА") or (name11 == "НЕТ" and name22 == "НЕТ") or
   (name11 == "да" and name22 == "да") or (name11 == "нет" and name22 == "нет")):
    print("ВЕРНО")
elif ((name11 == "ДА" and name22 == "НЕТ") or (name11 == "НЕТ" and name22 == "ДА") or
      (name11 == "да" and name22 == "нет") or (name11 == "нет" and name22 == "да")):
    print("ВЕРНО")
else:
    print("НЕВЕРНО")
