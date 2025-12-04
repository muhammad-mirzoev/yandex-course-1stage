total_sum = 0
count = 0

while True:
    try:
        height = input().strip()
        if height == "":
            break
        height = int(height)
        total_sum += height
        count += 1
    except ValueError:
        continue
    except EOFError:
        break

if count == 0:
    print(-1)
else:
    print(total_sum / count)
