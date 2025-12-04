flower_1 = input().strip()
flower_2 = input().strip()
flower_3 = input().strip()
bouquet_flowers = input().strip()

found_1 = flower_1 in bouquet_flowers
found_2 = flower_2 in bouquet_flowers
found_3 = flower_3 in bouquet_flowers

if found_1 or found_2 or found_3:
    result = "В букете есть"
    if found_1:
        result += f" {flower_1}"
    if found_2:
        if found_1:
            result += ","
        result += f" {flower_2}"
    if found_3:
        if found_1 or found_2:
            result += ","
        result += f" {flower_3}"
    result += "."
    print(result)
else:
    print("Таких цветов в букете нет.")

