N = int(input())

surname_count = {}

for _ in range(N):
    surname = input().strip()
    if surname in surname_count:
        surname_count[surname] += 1
    else:
        surname_count[surname] = 1

one_family_count = 0

for count in surname_count.values():
    if count > 1:
        one_family_count += count

print(one_family_count)
