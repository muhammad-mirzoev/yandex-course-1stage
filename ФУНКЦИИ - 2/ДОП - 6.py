def turbulence(left, right):
    def find_turbulence_index(arr):
        trend = None

        for i in range(1, len(arr)):
            if trend is None:
                if arr[i] > arr[i - 1]:
                    trend = True
                elif arr[i] < arr[i - 1]:
                    trend = False
            if trend is True and arr[i] < arr[i - 1]:
                return i
            elif trend is False and arr[i] > arr[i - 1]:
                return i
        return -1

    left_index = find_turbulence_index(left)
    right_index = find_turbulence_index(right)
    return left_index, right_index


# Пример использования
left = [1, 2, 2, 0, 3, 1]
right = [5, 4, 4, 3, 3, 2]
print(*turbulence(left, right))  # Ожидаемый вывод: 3 -1
