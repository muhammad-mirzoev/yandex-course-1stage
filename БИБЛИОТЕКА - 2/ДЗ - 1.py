from datetime import datetime, timedelta


def alarm(date_str, delta=10):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    base_date = datetime(2021, 1, 4)
    week_number = (date - base_date).days // 7 + 1

    if date.weekday() == 5 or date.weekday() == 6:
        if week_number % 2 == 1:
            alarm_time = "10:00"
        else:
            alarm_time = "11:00"
        return (alarm_time,)

    if week_number % 2 == 1:
        if date.weekday() == 0:
            alarm_time = "08:30"
        elif date.weekday() == 1:
            alarm_time = "08:30"
        elif date.weekday() == 2:
            alarm_time = "08:30"
        elif date.weekday() == 3:
            alarm_time = "07:45"
        elif date.weekday() == 4:
            alarm_time = "08:30"
    else:
        if date.weekday() == 0:
            alarm_time = "09:00"
        elif date.weekday() == 1:
            alarm_time = "09:00"
        elif date.weekday() == 2:
            alarm_time = "09:30"
        elif date.weekday() == 3:
            alarm_time = "09:30"
        elif date.weekday() == 4:
            alarm_time = "09:00"

    first_alarm = alarm_time
    second_alarm = (datetime.strptime(alarm_time, "%H:%M") + timedelta(minutes=delta)).strftime("%H:%M")

    return (first_alarm, second_alarm)


print(alarm("2021-1-4", 15))
print(alarm("2021-1-10"))
print(alarm("2021-1-11", 25))

