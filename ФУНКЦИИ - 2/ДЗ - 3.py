def prime(number):
    if number <= 1:
        return "Составное число"

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "Составное число"
    return "Простое число"


print(prime(4))  # Составное число
print(prime(3))  # Простое число
