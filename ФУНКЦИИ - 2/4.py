def average(values):
    values = values or [0]
    if (sum(values) / len(values)) == int(sum(values) / len(values)):
        return int(sum(values) / len(values))
    else:
        return sum(values) / len(values)


print(average([1, 2, 3, 4, 5]))
print(average([-5, 2]))
print(average([1, 5, 500, 10]))