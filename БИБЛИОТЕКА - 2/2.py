from datetime import datetime


def days_left(date_str):
    today = datetime.today()
    target_date = datetime.strptime(date_str, '%d.%m.%Y')
    delta = target_date - today

    return delta.days


print(days_left('31.12.2022'))
print(days_left('28.01.2022'))
