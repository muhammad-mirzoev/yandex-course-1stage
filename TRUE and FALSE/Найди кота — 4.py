n = int(input())

cat_found = False

for _ in range(n):
    line = input().strip()

    if "Кот" in line or "кот" in line:
        cat_found = True

    if "Пёс" in line or "пёс" in line:
        cat_found = False

if cat_found:
    print("МЯУ")
else:
    print("НЕТ")
