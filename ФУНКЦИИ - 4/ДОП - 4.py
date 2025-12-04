def sorting_bis(key, reverse):
    if key == "len":
        data.sort(key=len, reverse=reverse)
    elif key == "abc":
        data.sort(reverse=reverse)


# Пример 1
data = ["one", "two", "three"]
sorting_bis("len", True)
print(data)  # ['three', 'one', 'two']

# Пример 2
data = ["one", "two", "three"]
sorting_bis("abc", False)
print(data)  # ['one', 'three', 'two']
