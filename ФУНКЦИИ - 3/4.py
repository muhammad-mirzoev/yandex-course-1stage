current_receipt = []
receipt_counter = 1


def add_item(item_name, item_cost):
    current_receipt.append((item_name, item_cost))


def print_receipt():
    global current_receipt, receipt_counter

    if not current_receipt:
        return

    print(f"Чек {receipt_counter}. Всего предметов: {len(current_receipt)}")
    total_cost = 0

    for item_name, item_cost in current_receipt:
        print(f"{item_name} - {item_cost}")
        total_cost += item_cost

    print(f"Итого: {total_cost}")
    print("-----")
    current_receipt = []

    receipt_counter += 1


add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)