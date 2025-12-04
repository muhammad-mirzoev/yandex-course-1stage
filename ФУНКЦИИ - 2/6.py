def print_document(pages):
    secret_found = False

    for page in pages:
        if page.startswith("Секретно"):
            secret_found = True
            break
        print(page)
    if secret_found:
        print("Дальнейшие материалы засекречены")
    else:
        print("Напечатано без купюр")


print_document(["Обычная страница", "И еще страница", "Секретно Вот этот вот текст не показывать", "Никому", "Никогда"])
print_document(["Пустой трёп", "который", "никому не интересен"])
