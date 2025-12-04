N, total_sum = map(int, input().split())

calculated_sum = 0
incorrect_positions = []

for i in range(1, N + 1):
    line = input().strip()

    price_str, quantity_str, total_price_str = line.split()

    price = int(price_str.strip())
    quantity = int(quantity_str.strip('*'))
    total_price = int(total_price_str.strip('='))

    correct_price = price * quantity
    calculated_sum += correct_price

    if correct_price != total_price:
        incorrect_positions.append(i)

print(total_sum - calculated_sum)

if incorrect_positions:
    print(" ".join(map(str, incorrect_positions)))
