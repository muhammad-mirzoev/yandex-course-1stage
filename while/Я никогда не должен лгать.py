last_line = ""

while True:
    line = input()
    if line == "":
        break
    length = len(line)
    if 100 <= length <= 999:
        print(last_line)
    elif length % 2 == 0:
        print(line * 2)
    elif length % 3 == 0:
        print(line * 3)
    else:
        print(line)
    last_line = line