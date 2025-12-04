def month_name(month, language):
    months_en = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    months_ru = [
        "январь", "февраль", "март", "апрель", "май", "июнь",
        "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"
    ]

    if language == "en":
        return months_en[month - 1]
    elif language == "ru":
        return months_ru[month - 1]
    else:
        return


# Примеры использования:
print(month_name(3, "en"))  # March
print(month_name(3, "ru"))  # март
