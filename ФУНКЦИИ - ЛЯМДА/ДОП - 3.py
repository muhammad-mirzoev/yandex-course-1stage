def express(*stops):
    def should_stop(stop_data):
        index, name = stop_data
        if len(name) < 8:
            return True
        if len(set(name)) == len(name):
            return True
        if any(c.isdigit() and int(c) % 2 == 0 for c in name):
            return True
        if (index + 1) % 7 == 0:
            return True
        return False

    return list(filter(lambda name: not should_stop((stops.index(name), name)), stops))



data = ['Farringdon', 'Balham', 'Cathays-9', 'Teesside Airport-2', 'East Croydon-4', 'London Bridge-5', 'Heath-7', 'Beasdale-8', 'Butetown-4']
print(*express(*data), sep='\n')