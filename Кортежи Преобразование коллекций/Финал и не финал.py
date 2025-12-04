n = int(input())

teams = [(input(), int(input())) for _ in range(n)]

teams_sorted = sorted(teams, key=lambda x: x[1], reverse=True)

finalists_count = (n + 1) // 2

finalists = sorted(teams_sorted[:finalists_count], key=lambda x: x[0])
others = sorted(teams_sorted[finalists_count:], key=lambda x: x[0])

for team in finalists + others:
    print(team[0])
