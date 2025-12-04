base = ["Иван", "Юлия Иванкова"]


def hello(name):
    print(f"Здравствуйте, {name}! Вашу карту ищут...")


def search_card(name):
    if name in base:
        index = base.index(name) + 1
        print(f"Ваша карта с номером {index} найдена")
    else:
        print("Ваша карта не найдена")

# Пример использования
hello("Иван")
search_card("Иван")
hello("Юлия Иванкова")
search_card("Юлия Иванкова")
