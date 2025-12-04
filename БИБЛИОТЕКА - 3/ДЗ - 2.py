from PIL import Image, ImageDraw


def board(num, size):
    width = num * size
    height = num * size

    new_color = (255, 255, 255)
    newImage = Image.new("RGB", (width, height), new_color)
    draw = ImageDraw.Draw(newImage)

    for row in range(num):
        for col in range(num):
            if (row + col) % 2 == 0:
                color = (0, 0, 0)
            else:
                color = (255, 255, 255)

            x0 = col * size
            y0 = row * size
            x1 = x0 + size
            y1 = y0 + size
            draw.rectangle([x0, y0, x1, y1], fill=color)

    newImage.save("res.png")


board(8, 50)
