name = int(input())

total = 2 * name - 1

for i in range(1, name + 1):
    stars = 2 * i - 1
    spaces = (total - stars) // 2
    print(' ' * spaces + '*' * stars)
