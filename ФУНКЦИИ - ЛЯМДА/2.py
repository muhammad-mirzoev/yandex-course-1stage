def simple_map(transformation, values):
    result = []
    for value in values:
        result.append(transformation(value))
    return result


values = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, values))
