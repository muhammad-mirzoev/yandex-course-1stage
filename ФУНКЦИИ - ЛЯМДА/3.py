min_mass = int(input())
num_fields = int(input())
total_mass = 0

for _ in range(num_fields):
    field = list(map(int, input().split()))
    valid_berries = filter(lambda x: x >= min_mass, field)
    total_mass += sum(valid_berries)
print(total_mass)


# второй вариант
def collect_berries(min_mass, num_fields, fields):
    total_mass = 0
    for field in fields:
        valid_berries = filter(lambda x: x >= min_mass, field)
        total_mass += sum(valid_berries)
    return total_mass


min_mass = int(input())
num_fields = int(input())

fields = [list(map(int, input().split())) for _ in range(num_fields)]
result = collect_berries(min_mass, num_fields, fields)
print(result)
