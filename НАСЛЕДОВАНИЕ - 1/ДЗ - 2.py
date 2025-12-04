class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        print(f"Сообщение отправлено от {self.name} пользователю {user.name}: {message}")

    def post(self, message):
        print(f"{self.name} отправил пост на свою стену: {message}")

    def info(self):
        return ""

    def describe(self):
        print(f"Имя: {self.name}")
        additional_info = self.info()
        if additional_info:
            print(f"Дополнительная информация: {additional_info}")


class Person(User):
    def __init__(self, name, birthdate):
        super().__init__(name)
        self.birthdate = birthdate

    def info(self):
        return f"Дата рождения: {self.birthdate}"

    def subscribe(self, user):
        print(f"{self.name} подписался на {user.name}")


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f"Описание: {self.description}"
