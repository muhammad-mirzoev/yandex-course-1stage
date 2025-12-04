phone_number = input().strip()
total_number = f"+1({phone_number[:3]}){phone_number[3:6]}-{phone_number[6:]}"

print(total_number)