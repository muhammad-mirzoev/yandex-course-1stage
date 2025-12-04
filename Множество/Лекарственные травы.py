n = int(input())

herbs = set()

for _ in range(n):
    m = int(input())
    for _ in range(m):
        herb = input().strip()
        herbs.add(herb)

for herb in herbs:
    print(herb)
