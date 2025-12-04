n = int(input())
milk_amounts = [int(input()) for _ in range(n)]
min_milk = int(input())
max_milk = int(input())

for milk in milk_amounts:
    if min_milk <= milk <= max_milk:
        print(milk)
