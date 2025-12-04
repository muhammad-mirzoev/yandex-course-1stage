from PIL import Image, ImageDraw


# Функция для рисования мухомора
def draw_mushroom(background_color, cell_size):
    # Размер изображения
    width, height = 20, 22
    img_width = width * cell_size
    img_height = height * cell_size

    # Создание изображения с фоном
    img = Image.new("RGB", (img_width, img_height), tuple(background_color))  # Передаем как кортеж
    draw = ImageDraw.Draw(img)

    # Цвета
    cap_color = (192, 0, 0)
    stem_color = (255, 250, 235)
    dot_color = (255, 255, 255)
    grass_color = (146, 208, 80)

    # Рисование шляпки (верхняя часть мухомора)
    cap_top = (5, 2)  # Начало верхней шляпки (координаты в клетках)
    cap_bottom = (15, 7)  # Нижний край шляпки (координаты в клетках)

    # Заполнение шляпки красным
    for i in range(cap_top[1], cap_bottom[1] + 1):
        for j in range(cap_top[0], cap_bottom[0] + 1):
            draw.rectangle([j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size], fill=cap_color)

    # Рисование точек на шляпке
    dot_positions = [(7, 3), (9, 3), (8, 4), (6, 5), (10, 5)]
    for (i, j) in dot_positions:
        draw.rectangle([j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size], fill=dot_color)

    # Рисование ножки (трубка)
    stem_top = (9, 7)
    stem_bottom = (11, 14)

    # Заполнение ножки светло-желтым
    for i in range(stem_top[1], stem_bottom[1] + 1):
        for j in range(stem_top[0], stem_bottom[0] + 1):
            draw.rectangle([j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size], fill=stem_color)

    # Рисование травы
    for i in range(17, 22):
        for j in range(0, 20):
            draw.rectangle([j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size], fill=grass_color)

    return img


# Ввод
background_color = list(map(int, input().split()))  # Цвет фона
cell_size = int(input())  # Размер клетки

# Получаем изображение
img = draw_mushroom(background_color, cell_size)

# Сохраняем изображение
output_path = "mushroom.png"
img.save(output_path)

# Выводим путь к файлу
print(f"Изображение сохранено как {output_path}")
