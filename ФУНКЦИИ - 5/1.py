def matrix(n=1, m=None, a=0):
    if m is None:
        m = n
    return [[a for _ in range(m)] for _ in range(n)]


rows = matrix()
for row in rows:
    print(*row)
rows = matrix(2)
for row in rows:
    print(*row)