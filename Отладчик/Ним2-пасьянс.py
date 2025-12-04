first_pile = int(input())
second_pile = int(input())

while True:
    pile_number = int(input())
    if pile_number == 1:
        stones = int(input())
        first_pile -= stones
    else:
        stones = int(input())
        second_pile -= stones

    print(first_pile, second_pile)

    if first_pile == 0 and second_pile == 0:
        break