log = ['Иванов', 'Кузнецов', 'Петрова']
called = set()


def pupil_number(surname):
    if surname in log:
        print(log.index(surname) + 1)
    else:
        print("Такого ученика нет.")


def add_pupil(surname):
    if surname not in log:
        log.append(surname)
        log.sort()
        print(f"Ученик {surname} добавлен.")
    else:
        print("Такой ученик уже есть в журнале.")


def to_the_blackboard(n):
    if n < 1 or n > len(log):
        print("Некорректный номер ученика.")
        return

    surname = log[n - 1]

    if surname in called:
        print("Сан Саныч, Вы меня уже вызывали!")
    else:
        called.add(surname)
        print(f"{surname}, к доске!")


log = ['Иванов', 'Кузнецов', 'Петрова']
pupil_number("Петрова")
add_pupil("Смирнов")
add_pupil("Иванов")
to_the_blackboard(4)
add_pupil("Васильев")
pupil_number("Смирнов")
to_the_blackboard(5)