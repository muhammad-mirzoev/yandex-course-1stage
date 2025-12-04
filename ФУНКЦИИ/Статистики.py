def mean(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)


def median(arr):
    if len(arr) == 0:
        return 0
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 1:
        return arr_sorted[n // 2]
    else:
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2


def print_statistics(arr):
    if len(arr) == 0:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        return

    print(len(arr))
    print(mean(arr))
    print(min(arr))
    print(max(arr))
    print(median(arr))
