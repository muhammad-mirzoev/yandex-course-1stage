import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Введите характерный размер
s = 10

# Размер изображения
fig, ax = plt.subplots(figsize=(7, 7), dpi=s * 10)
ax.set_xlim(0, 70 * s)
ax.set_ylim(0, 70 * s)
ax.set_aspect('equal')
ax.axis('off')

# Цвета
bg_color = (1, 1, 1)  # белый
circle_color = (0/255, 112/255, 192/255)
top_snake_color = (1, 1, 1)
bottom_snake_color = (255/255, 192/255, 0)

# Заливка фона
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

# Рисуем круги
circle_radius = 30 * s
center1 = (25 * s, 35 * s)
center2 = (45 * s, 35 * s)

circle1 = patches.Circle(center1, circle_radius, color=circle_color)
circle2 = patches.Circle(center2, circle_radius, color=circle_color)
ax.add_patch(circle1)
ax.add_patch(circle2)

# Верхняя "змейка" (белая)
top_snake = patches.FancyBboxPatch(
    (10 * s, 35 * s), 25 * s, 20 * s,
    boxstyle="round,pad=0.5",
    color=top_snake_color
)
ax.add_patch(top_snake)

# Нижняя "змейка" (жёлтая)
bottom_snake = patches.FancyBboxPatch(
    (35 * s, 15 * s), 25 * s, 20 * s,
    boxstyle="round,pad=0.5",
    color=bottom_snake_color
)
ax.add_patch(bottom_snake)

# Сохраняем изображение
plt.savefig("python_logo.png", dpi=s * 10, bbox_inches='tight')
plt.close()
