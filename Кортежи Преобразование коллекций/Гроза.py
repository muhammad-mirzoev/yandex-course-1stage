n = int(input())

places = []
for _ in range(n):
    height = int(input())
    iron_content = float(input())
    places.append((height, iron_content))

for i in range(n):
    for j in range(n - 1 - i):
        if places[j][0] < places[j + 1][0] or (places[j][0] == places[j + 1][0] and places[j][1] < places[j + 1][1]):
            places[j], places[j + 1] = places[j + 1], places[j]

for place in places:
    print(place)
