lastTicket = 123321


def lucky(ticket):
    ticket_str = str(ticket).zfill(6)

    def is_lucky(ticket_str):
        first_sum = sum(int(digit) for digit in ticket_str[:3])
        last_sum = sum(int(digit) for digit in ticket_str[3:])
        return first_sum == last_sum

    if is_lucky(ticket_str) and is_lucky(str(lastTicket).zfill(6)):
        return "Счастливый"
    else:
        return "Несчастливый"


lastTicket = 123456
print(lucky(100001))
lastTicket = 123321
print(lucky(100001))