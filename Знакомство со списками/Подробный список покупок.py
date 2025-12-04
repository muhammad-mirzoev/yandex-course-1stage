n = int(input().strip())

purchases = []

for _ in range(n):
    name = input().strip()
    quantity = input().strip()
    purchases.append(f"{name} {quantity}")

for purchase in reversed(purchases):
    print(purchase)
