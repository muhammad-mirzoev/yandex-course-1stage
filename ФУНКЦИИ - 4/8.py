def dried_apricots(lst):
    def f(x, y):
        tmp = [j if j > i else 0 if not i or not j or i / j >= 2 else i for i, j in zip(x, y)]
        return tmp

    apricots[:] = f(apricots, lst)


apricots = [3, 5, 7.5, 18]
dried_apricots([1.5, 5.1, 3.74, 15])
print(apricots)
dried_apricots([0, 2.6, 0, 8])
print(apricots)
dried_apricots([0, 2.45, 0, 0])
print(apricots)
