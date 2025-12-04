n = int(input())

numbers = [int(input()) for _ in range(n)]

target = int(input())

num_set = set(numbers)

for num in numbers:
    if target % num == 0:
        second_factor = target // num
        if second_factor in num_set:
            if (second_factor != num) or numbers.count(num) > 1:
                print("ДА")
                exit()

print("НЕТ")
