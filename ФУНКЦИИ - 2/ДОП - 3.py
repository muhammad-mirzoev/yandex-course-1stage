def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def catalan(n):
    return factorial(2 * n) // (factorial(n) * factorial(n + 1))

# Пример использования
print(catalan(0))  # Вывод: 1
print(catalan(1))  # Вывод: 1
print(catalan(2))  # Вывод: 2
print(catalan(3))  # Вывод: 5
