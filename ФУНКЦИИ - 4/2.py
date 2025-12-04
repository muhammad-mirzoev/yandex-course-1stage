daily_food = [0, 150, 150]

def count_food(days):
    total_cost = 0
    for day in days:
        total_cost += daily_food[day - 1]
    return total_cost


print(count_food([1]))
print(count_food([2, 3]))
