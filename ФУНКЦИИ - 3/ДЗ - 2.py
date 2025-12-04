profile = {}


def setup_profile(name, vacation_dates):
    global profile
    profile = {"name": name, "vacation_dates": vacation_dates}


def print_application_for_leave():
    print(f"Заявление на отпуск в период {profile['vacation_dates']}. {profile['name']}")


def print_holiday_money_claim(amount):
    print(f"Прошу выплатить {amount} отпускных денег. {profile['name']}")


def print_attorney_letter(to_whom):
    print(f"На время отпуска в период {profile['vacation_dates']}"
          f" моим заместителем назначается {to_whom}. {profile['name']}")


setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")