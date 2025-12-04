number = input()

stars = ['*' * int(digit) for digit in number]
for star in stars:
    print(star)
