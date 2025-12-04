base = ["Иван", "Юлия Иванкова"]
query = [None, None, None]


def hello(name):
    for i in range(len(query)):
        if query[i] is None:
            query[i] = name
            print(f"Здравствуйте, {name}! Подойдите к окошку номер {i + 1}")
            return
    print(f"Простите, {name}. Все окна заняты")


def search_card(name):
    if name not in query:
        print(f"Простите, {name}, дождитесь своей очереди")
        return
    card_number = base.index(name) + 1
    if card_number <= len(base):
        print(f"Ваша карта с номером {card_number} найдена")
    else:
        print("Ваша карта не найдена")


def good_bye(name):
    for i in range(len(query)):
        if query[i] == name:
            query[i] = None
            print(f"До свидания, не болейте, {name}")
            return
    print(f"Простите, {name}, дождитесь своей очереди")


hello("Иван")
search_card("Иван")
hello("Юлия Иванкова")
search_card("Юлия Иванкова")
