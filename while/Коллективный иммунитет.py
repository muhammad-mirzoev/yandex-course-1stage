yes_count = 0
total_count = 0

while True:
    line = input().strip()
    if line == "":
        break
    if line == "да":
        yes_count += 1
    total_count += 1

if yes_count / total_count >= 0.8:
    print("Достигли")
else:
    print("Пока нет")
