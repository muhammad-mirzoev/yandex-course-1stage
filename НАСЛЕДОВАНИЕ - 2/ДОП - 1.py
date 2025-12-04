class Service:
    def __init__(self, address, event_id):
        self.address = address
        self.id = event_id

    def arrival_time(self):
        return len(self.address)

    def get(self):
        return {'address': self.address, 'id': self.id}


class Ambulance(Service):
    def __init__(self, address, event_id, mode, severity):
        super().__init__(address, event_id)
        self.mode = mode
        self.severity = severity

    def get(self):
        data = super().get()
        data.update({'mode': self.mode, 'severity': self.severity})
        return data


class Firefighters(Service):
    def __init__(self, address, event_id, mode, victims):
        super().__init__(address, event_id)
        self.mode = mode
        self.victims = victims

    def get(self):
        data = super().get()
        data.update({'mode': self.mode, 'victims': self.victims})
        return data


class Police(Service):
    def __init__(self, address, event_id, mode, victims, armament_required):
        super().__init__(address, event_id)
        self.mode = mode
        self.victims = victims
        self.armament_required = armament_required

    def get(self):
        data = super().get()
        data.update({'mode': self.mode, 'victims': self.victims, 'armament_required': self.armament_required})
        return data


# Пример использования
serv = Service("Red Square, 1", 1)
print(serv.get())  # {'address': 'Red Square, 1', 'id': 1}
print(serv.arrival_time())  # 13

amb = Ambulance("Bolshaya Gruzinskaya str., 1", 2, 5, 0)
print(amb.get())  # {'address': 'Bolshaya Gruzinskaya str., 1', 'id': 2, 'mode': 5, 'severity': 0}
print(amb.arrival_time())  # 28

pol = Police("Tverskaya St., 13, Moscow, Russia", 3, 1, 0, False)
print(pol.get())  # {'address': 'Tverskaya St., 13, Moscow, Russia', 'id': 3, 'mode': 1, 'victims': 0, 'armament_required': False}
print(pol.arrival_time())  # 33
