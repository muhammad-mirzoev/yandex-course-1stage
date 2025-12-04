import datetime


def days_to_the_next_flight(first, second, third, today=None):
    if today is None:
        today = datetime.date.today()

    year = today.year
    month = today.month

    flight_days = [first, second, third]
    possible_flight_dates = []

    for day in flight_days:
        try:
            flight_date = datetime.date(year, month, day)
        except ValueError:
            if month == 12:
                flight_date = datetime.date(year + 1, 1, day)
            else:
                flight_date = datetime.date(year, month + 1, day)
        if flight_date == today:
            continue
        if flight_date.weekday() == 3:
            flight_date += datetime.timedelta(days=2)
        if flight_date < today:
            if month == 12:
                new_year, new_month = year + 1, 1
            else:
                new_year, new_month = year, month + 1
            try:
                flight_date = datetime.date(new_year, new_month, day)
            except ValueError:
                continue
            if flight_date.weekday() == 3:
                flight_date += datetime.timedelta(days=2)
            if flight_date == today:
                continue
        possible_flight_dates.append(flight_date)
    if not possible_flight_dates:
        return None

    return min((date - today).days for date in possible_flight_dates)




print(days_to_the_next_flight(28, 14, 9, today=datetime.date(2282,12,28)))
