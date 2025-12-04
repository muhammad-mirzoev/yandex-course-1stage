def take_large_banknotes(banknotes):
    bank = list()
    for s in banknotes:
        if s > 10:
            bank.append(s)
    return bank


print(*take_large_banknotes([1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]))
