import datetime as dt

hm_days = int(input())
my_date = dt.datetime.now()

new_date = dt.timedelta(days=hm_days) + my_date
print(new_date.day, new_date.month)
