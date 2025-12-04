def secret_sort():
    dct = {}
    for key in secret_avatars:
        dct[key] = len([let for i, let in enumerate(key) if i % 2 and let.lower() in 'eyuoai'])
    n = len(secret_avatars)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if dct.get(secret_avatars[j]) > dct.get(secret_avatars[j + 1]):
                secret_avatars[j], secret_avatars[j + 1] = secret_avatars[j + 1], secret_avatars[j]


secret_avatars = ['March Hare', 'Hatter', 'Dormouse', 'Alice']
secret_sort()
print(secret_avatars)
secret_avatars = ['Benedict Cumberbatch', 'Sean Bean', 'Jhonny Depp', 'Daniel Radcliffe', 'Orlando Bloom']
secret_sort()
print(secret_avatars)