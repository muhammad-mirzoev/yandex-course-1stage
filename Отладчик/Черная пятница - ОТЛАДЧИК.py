current_discount = int(input())

if current_discount == 0:
    new_discount = 50
elif current_discount <= 30:
    new_discount = current_discount + (current_discount // 2)
elif current_discount <= 70:
    new_discount = current_discount + (current_discount // 10)
else:
    new_discount = current_discount

print(new_discount)
