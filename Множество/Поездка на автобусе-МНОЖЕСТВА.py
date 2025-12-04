first_list = set()
while True:
    num = input().strip()
    if num == "":
        break
    first_list.add(num)

second_list = set()
while True:
    num = input().strip()
    if num == "":
        break
    second_list.add(num)

common_numbers = first_list & second_list

if common_numbers:
    for num in sorted(common_numbers, key=int):
        print(num)
else:
    print("EMPTY")
