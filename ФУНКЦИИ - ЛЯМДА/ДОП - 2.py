def smart_search(*args, func):
    if all(isinstance(x, int) for x in args):
        return tuple(filter(func, args))
    elif all(isinstance(x, str) for x in args):
        return tuple(x for x in args if x[0].isupper())


print(smart_search(1, 2, 3, 5, 12, func=lambda x: x % 2))
# Вывод: (1, 3, 5)
print(smart_search('The', 'quick', 'brown', 'Fox', 'jumps', 'over', 'the', 'Lazy', 'Dog', func=lambda x: x))
# Вывод: ('The', 'Fox', 'Lazy', 'Dog')
