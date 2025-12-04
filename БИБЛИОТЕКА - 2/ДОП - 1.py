from datetime import datetime, date


def asteroid_angle(n):
    data1 = date.today()
    data2 = date(2000, 1, 1)
    if data1 != date.today():
        data1 = datetime.datetime.strptime(data1, '%Y-%m-%d')
        g = round(360 / n * ((data1 - data2).days % n))
    else:
        g = round(360 / n * ((data1 - data2).days % n))
    return g

# Проверка
print(asteroid_angle(220))  # Ожидаемый результат: 190
print(asteroid_angle(2009)) # Ожидаемый результат: 0
