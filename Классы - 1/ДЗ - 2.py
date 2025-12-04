class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\n{self.content}"


class MailServer:
    def __init__(self, name):
        self.name = name
        self.users = {}

    def add_user(self, user):
        if user not in self.users:
            self.users[user] = []

    def receive_mail(self, user):
        if user in self.users and self.users[user]:
            return self.users[user].pop(0)
        return None

    def store_mail(self, user, message):
        if user not in self.users:
            self.add_user(user)
        self.users[user].append(message)

    def __str__(self):
        return f"MailServer({self.name})"


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user
        self.server.add_user(user)

    def receive_mail(self):
        message = self.server.receive_mail(self.user)
        if message:
            print("Received message:")
            print(message)
        else:
            print("No new messages.")

    def send_mail(self, server, user, message):
        if server not in mail_system.servers:
            print(f"Cannot send mail to {server}. Server not found.")
            return
        server.store_mail(user, message)
        print(f"Sent message to {user}@{server.name}")


class MailSystem:
    def __init__(self):
        self.servers = {}

    def add_server(self, server):
        self.servers[server] = server

    def get_server(self, name):
        return self.servers.get(name)


# Создаем почтовую систему
mail_system = MailSystem()

# Создаем серверы
server1 = MailServer("server1.com")
server2 = MailServer("server2.com")

# Добавляем серверы в систему
mail_system.add_server(server1)
mail_system.add_server(server2)

# Создаем клиентов
client1 = MailClient(server1, "user1")
client2 = MailClient(server2, "user2")

# Отправляем письмо от клиента 1 на сервер 2
message = Message("user1", "user2", "Hello from user1 to user2!")
client1.send_mail(server2, "user2", message)

# Клиент 2 получает письмо
client2.receive_mail()
