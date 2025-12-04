n = int(input())
error_count = 0
correct_count = 0
expected = "раз"

while error_count < n:
    count = input().strip()
    if count == expected:
        correct_count += 1
        if expected == "раз":
            expected = "два"
        elif expected == "два":
            expected = "три"
        elif expected == "три":
            expected = "четыре"
        else:
            expected = "раз"
    else:
        print(f"Правильных отсчётов было {correct_count}, но теперь вы ошиблись.")
        error_count += 1
        correct_count = 0
        expected = "раз"

    if error_count == n:
        print("На сегодня хватит.")
        break
