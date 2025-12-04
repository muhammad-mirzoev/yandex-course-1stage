from PIL import Image


def mirror():
    img = Image.open('image.jpg')
    width, height = img.size
    result = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            result.putpixel((height - 1 - y, width - 1 - x), pixel)
    result.save('res.jpg')


mirror()
