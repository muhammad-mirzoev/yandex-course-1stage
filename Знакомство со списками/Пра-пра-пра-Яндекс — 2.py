n = int(input())
data_lines = [input() for _ in range(n)]
m = int(input())
search_strings = [input() for _ in range(m)]

for line in data_lines:
    if all(s in line for s in search_strings):
        print(line)