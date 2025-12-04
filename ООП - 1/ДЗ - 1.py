class BigBell:
    def __init__(self):
        self.toggle = True

    def sound(self):
        if self.toggle:
            print("ding")
        else:
            print("dong")
        self.toggle = not self.toggle


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()