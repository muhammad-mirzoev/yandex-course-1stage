divisors = {}


def number_of_divisors(n):
    if n in divisors:
        return divisors[n]
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    divisors[n] = count
    return count


# Тестирование
print(number_of_divisors(2000000000))  # 110
print(number_of_divisors(6))  # 4
print(number_of_divisors(6))  # 4
print(number_of_divisors(2000000000))  # 110
print(divisors)  # {2000000000: 110, 6: 4}
