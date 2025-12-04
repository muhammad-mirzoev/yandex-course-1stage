class MinStat:
    def __init__(self):
        self.min_value = None

    def add_number(self, number):
        if self.min_value is None or number < self.min_value:
            self.min_value = number

    def result(self):
        return self.min_value


class MaxStat:
    def __init__(self):
        self.max_value = None

    def add_number(self, number):
        if self.max_value is None or number > self.max_value:
            self.max_value = number

    def result(self):
        return self.max_value


class AverageStat:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_number(self, number):
        self.total += number
        self.count += 1

    def result(self):
        if self.count == 0:
            return None
        return self.total / self.count


mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())