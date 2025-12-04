def drug(y):
    y = y.split()[-1]
    con = y[-3:]
    if con == 'ino':
        y = y[:-3] + 'lone'
    else:
        y = y[:-2] + 'ino'
    return y


print(*list(map(drug, filter(lambda x: len(x.split()) > 1, input().split('; ')))), sep=', ')
