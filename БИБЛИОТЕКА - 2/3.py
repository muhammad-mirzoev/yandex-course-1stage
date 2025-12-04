from datetime import datetime, timedelta
import math


cost = int(input())
discount = int(input())
delivery_days = int(input())
order_date_str = input()
order_time_str = input()

order_date = datetime.strptime(order_date_str, "%d.%m.%Y")
order_time = datetime.strptime(order_time_str, "%H:%M")

if 6 <= order_time.hour < 12 or (order_time.hour == 12 and order_time.minute <= 30):
    if order_date.weekday() == 0:
        discounted_price = math.floor(cost - (cost * discount / 100))
    else:
        discounted_price = math.floor(cost - (cost * discount / 100))
        delivery_days -= 1
else:
    discounted_price = cost

delivery_date = order_date + timedelta(days=delivery_days)
delivery_date_str = delivery_date.strftime("%d-%m-%Y")

print(f"{delivery_date_str} {discounted_price}")
