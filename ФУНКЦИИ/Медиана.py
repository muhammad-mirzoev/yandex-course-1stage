def median(x: list) -> [int, float]:
    print(sorted(x)[len(x) // 2] if len(x) % 2 else sum(sorted(x)[len(x) // 2 - 1:len(x) // 2 + 1]) / 2)


data = [1, 5, 4, 2, 3]
median(data)

data = [3, 2, 4, 1]
median(data)