from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    event = input().strip()

    if event.startswith("Кто последний?"):
        surname = event.split("Я - ")[1][:-1]
        queue.append(surname)

    elif event.startswith("Я только спросить!"):
        surname = event.split("Я - ")[1][:-1]
        queue.appendleft(surname)

    elif event == "Следующий!":
        if queue:
            print(f"Заходит {queue.popleft()}!")
        else:
            print("В очереди никого нет.")
