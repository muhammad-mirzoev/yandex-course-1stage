class Controller:
    def __init__(self):
        self.channel = 1

    def click(self):
        self.channel = (self.channel % 5) + 1


c = Controller()
c.click()
c.click()
print(c.channel)
c.click()
c.click()
print(c.channel)