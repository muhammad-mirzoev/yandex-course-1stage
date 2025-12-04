class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0

    def add_left(self, weight):
        self.left_weight += weight

    def add_right(self, weight):
        self.right_weight += weight

    def result(self):
        if self.left_weight > self.right_weight:
            return "L"
        elif self.left_weight < self.right_weight:
            return "R"
        else:
            return "="