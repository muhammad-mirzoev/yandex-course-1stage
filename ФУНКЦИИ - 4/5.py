def rests(divisor):
    return [x % divisor for x in lst]


lst = [42, 17, 34, 100501]
print(*rests(3))  # 0 2 1 1
print(*lst)  # 42 17 34 100501
