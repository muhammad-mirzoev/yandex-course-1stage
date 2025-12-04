def horse(curr, wp):
    dx = abs(ord(curr[0]) - ord(wp[0]))
    dy = abs(int(curr[1]) - int(wp[1]))
    if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
        print(True)
    else:
        print(False)
horse('d4', 'b3')
horse('d4', 'a3')