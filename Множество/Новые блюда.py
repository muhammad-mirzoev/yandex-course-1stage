M = int(input())
all_dishes = set(input().strip() for _ in range(M))

N = int(input())
prepared_dishes = set()

for _ in range(N):
    day_dishes_count = int(input())
    day_dishes = set(input().strip() for _ in range(day_dishes_count))
    prepared_dishes.update(day_dishes)

unprepared_dishes = all_dishes - prepared_dishes

for dish in unprepared_dishes:
    print(dish)
