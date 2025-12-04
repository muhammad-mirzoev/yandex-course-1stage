import re

s = input()
if re.match(r'^[A-H][1-8]-[A-H][1-8]$', s):
    x1, y1, _, x2, y2 = map(ord, s)
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('YES')
    else:
        print('NO')
else:
    print('ERROR')
