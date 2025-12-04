class Holiday:
    seasons = {
        'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
        'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
        'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
        'September': 'Autumn', 'October': 'Autumn', 'November': 'Autumn'
    }

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.date}')"

    def get_season(self):
        month = self.date.split()[1]
        return self.seasons[month]


class NewYear(Holiday):
    def __init__(self, name, date, people):
        super().__init__(name, date)
        self.people = list(people)

    def congratulate(self, name):
        if name in self.people:
            return f"Dear {name}! Happy New Year!"
        else:
            self.people.append(name)
            return f"Dear new friend {name}! Have fun this New Year!"

    def get_greet(self):
        return self.people

    def __str__(self):
        return f"NewYear('{self.name}', '{self.date}')"


class MuseumDay(Holiday):
    def __init__(self, name, date, museums):
        super().__init__(name, date)
        self.museums = list(museums)

    def get_museums(self):
        return self.museums

    def __str__(self):
        return f"MuseumDay('{self.name}', '{self.date}')"


# Пример использования

hl = Holiday('1st Year Day', '1 January')
print(hl, hl.get_season(), sep='\n')

people = ['Kiang', 'Li', 'Meyfen']
ny = NewYear('Chinese New Year', '1 March', people)
print(ny, ny.congratulate('Song'), ny.congratulate('Li'), sep='\n')

museums = ["New Acropolis", "Mars", "Artists' Town", "Central House of the Writer"]
md = MuseumDay('International Museum Day', '18 May', museums)
print(', '.join(sorted(md.get_museums())))
print(ny.get_season())
print(md.get_season())
