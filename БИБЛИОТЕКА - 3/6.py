import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Характерный размер
s = 20  # Можно заменить на любое другое целое число

# Цвета
green = "#00b050"
brown = "#7f6000"

# Размеры дерева на основе масштаба s
trunk_width = s
trunk_height = s
triangle_height = s
triangle_width = s * 3

# Создаем изображение
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_xlim(0, triangle_width + s)
ax.set_ylim(0, triangle_height * 3 + trunk_height + s)

# Треугольники (еловые ярусы)
for i in range(3):
    base_y = trunk_height + i * triangle_height
    triangle = patches.Polygon([
        (s + triangle_width / 2, base_y + triangle_height),  # верхушка
        (s, base_y),  # левый угол
        (s + triangle_width, base_y)  # правый угол
    ], closed=True, color=green)
    ax.add_patch(triangle)

# Ствол
trunk = patches.Rectangle(
    (s + triangle_width / 2 - trunk_width / 2, 0),
    trunk_width, trunk_height,
    color=brown
)
ax.add_patch(trunk)

# Убираем оси и сохраняем файл
ax.axis('off')
plt.savefig("fir_tree.png", bbox_inches='tight', pad_inches=0)
plt.close()

print("Изображение сохранено в файле fir_tree.png.")
