target_x = int(input())
target_y = int(input())

if target_x == 0 and target_y == 0:
    print(0)
else:
    current_x = 0
    current_y = 0

    steps_count = 0

    while True:
        direction = input().strip()

        if direction == "стоп":
            break

        steps = int(input().strip())

        if direction == "север":
            current_y += steps
        elif direction == "юг":
            current_y -= steps
        elif direction == "восток":
            current_x += steps
        elif direction == "запад":
            current_x -= steps

        steps_count += 1

        if current_x == target_x and current_y == target_y:
            print(steps_count)
            break