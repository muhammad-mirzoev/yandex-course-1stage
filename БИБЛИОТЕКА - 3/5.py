from PIL import Image
import math

image = Image.open('yoda.png')
pixels = image.load()

n = int(input())
width, height = image.size

for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        max_diff = max(r, g, b) - min(r, g, b)
        change = max_diff // n

        r_new = max(0, min(255, r + change))
        g_new = max(0, min(255, g + change))
        b_new = max(0, min(255, b + change))

        pixels[x, y] = (r_new, g_new, b_new)

image.save('sense.png')
