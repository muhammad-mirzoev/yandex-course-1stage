def space_game(text):
    spaces_count = text.count(' ')

    if spaces_count % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")