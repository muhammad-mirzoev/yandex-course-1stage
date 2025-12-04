def typification(data):
    result = {}

    for item in data:
        item_type = type(item).__name__  # Получаем имя типа элемента

        # Если этот тип уже есть в словаре, добавляем элемент в список
        if item_type in result:
            result[item_type].append(item)
        else:
            result[item_type] = [item]  # Иначе создаем новый список с элементом

    return result


data = [3, 'xzy', 'abc', {'1': 's'}, [1, 2, 3], -2.5, 14, {'a': 1}]
print(typification(data))
