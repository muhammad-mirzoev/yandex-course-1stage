name = float(input())

if name < 0:
    print("Пуск")
else:
    for i in range(name, -1, -1):
        print(f"Осталось секунд: {i}")
    print("Пуск")