class Date:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day):
        self.month = month
        self.day = day

    def _to_day_of_year(self):
        return sum(self.days_in_month[:self.month - 1]) + self.day

    def __sub__(self, other):
        return self._to_day_of_year() - other._to_day_of_year()


jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)
