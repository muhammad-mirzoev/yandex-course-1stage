n = int(input())

# Считываем сам "белый список"
white_list = set(input().strip() for _ in range(n))
m = int(input())

for _ in range(m):
    query = input().strip()
    if query in white_list:
        print(query)
