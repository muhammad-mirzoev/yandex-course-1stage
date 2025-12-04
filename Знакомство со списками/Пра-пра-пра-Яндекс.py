n = int(input())
data = [input() for _ in range(n)]

search_query = input()

for line in data:
    if search_query in line:
        print(line)
