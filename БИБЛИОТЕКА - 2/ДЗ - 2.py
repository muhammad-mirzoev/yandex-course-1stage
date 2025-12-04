import math
from datetime import datetime

periods = {
    'physical': 23,
    'emotional': 28,
    'intellectual': 33
}


def calculate_biorhythm(birth_date, target_date, period):
    delta_days = (target_date - birth_date).days
    biorhythm_value = math.sin((2 * math.pi * delta_days) / period) * 100
    return round(biorhythm_value, 2)


def main():
    birth_date_str = input()
    target_date_str = input()
    birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
    target_date = datetime.strptime(target_date_str, "%d.%m.%Y")
    for period in periods.values():
        print(calculate_biorhythm(birth_date, target_date, period))


if __name__ == "__main__":
    main()
