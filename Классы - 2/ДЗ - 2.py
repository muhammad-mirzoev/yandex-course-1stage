criterions = ['x > 0', 'x%5==0', 'True']
functions = [lambda x: -x, lambda x: x * x, lambda x: x + 1]
critfun_of_comm = {'make_negative': (0, 0),
                   'square': (2, 1),
                   'strange_command': (1, 2)}


def f(critfun, list_):
    for i, x in enumerate(list_):
        if eval(criterions[critfun[0]]):
            list_[i] = functions[critfun[1]](x)
    return list_


*arr, = map(int, input().split())
for _ in range(int(input())):
    arr = f(critfun_of_comm[input()], arr)

print(*arr)