number = int(input().strip())

a = number // 100
b = (number // 10) % 10
c = number % 10

min_digit = min(a, b, c)
max_digit = max(a, b, c)

remaining_digit = a + b + c - min_digit - max_digit

half_sum = (min_digit + max_digit) / 2

if half_sum == remaining_digit:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")


