bets = {}


def do_bet(horse_number, bet_amount):
    if bet_amount <= 0:
        print("Что-то пошло не так, попробуйте еще раз")
    elif horse_number < 1 or horse_number > 10:
        print("Что-то пошло не так, попробуйте еще раз")
    elif horse_number in bets:
        print("Что-то пошло не так, попробуйте еще раз")
    else:
        bets[horse_number] = bet_amount
        print(f"Ваша ставка в размере {bet_amount} на лошадь {horse_number} принята")


do_bet(1, 10)
do_bet(1, 100)
do_bet(2, 0)
do_bet(2, 200)
