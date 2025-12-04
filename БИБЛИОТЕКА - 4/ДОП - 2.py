from PIL import Image, ImageOps


def create_tile_with_ornament(ornament_path, s):
    # Загрузка орнамента
    ornament = Image.open(ornament_path)

    # Вычисление размеров плитки и рамки
    frame_size = s // 10
    tile_size = s - 2 * frame_size

    # Изменяем размер орнамента, чтобы он подходил для плитки с учетом рамки
    ornament_resized = ornament.resize((tile_size, tile_size), Image.LANCZOS)

    # Создаем плитку с рамкой
    tile = Image.new('RGB', (s, s), (32, 32, 32))  # Цвет фона плитки
    tile.paste(ornament_resized, (frame_size, frame_size))

    # Создаем рамку
    frame = Image.new('RGB', (s, s), '#208d80')

    # Вставляем орнамент в плитку
    tile_with_frame = Image.composite(tile, frame, Image.new('1', (s, s), 255))

    # Сохраняем результат
    tile_with_frame.save('tile.png')


# Пример вызова функции
create_tile_with_ornament('ornament.png', 400)
