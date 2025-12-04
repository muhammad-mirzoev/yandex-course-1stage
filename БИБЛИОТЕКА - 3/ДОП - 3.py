from PIL import Image, ImageDraw

color = input()
numbers = input()


def HEXtoRGB(hex: str):
    hexColor = hex.lstrip('#')
    return tuple(int(hexColor[i: i + 2], 16) for i in (0, 2, 4))


color = HEXtoRGB(color)

image = Image.new("RGB", (630, 320), color)
drawer = ImageDraw.Draw(image)

for i in range(6):
    drawer.rectangle((60 + i * 90, 100, 120 + i * 90, 220), outline=HEXtoRGB("#bfbfbf"), width=1)
    drawer.line((60 + i * 90, 160, 120 + i * 90, 160), HEXtoRGB("#bfbfbf"))
    drawer.line((60 + i * 90, 160, 120 + i * 90, 100), HEXtoRGB("#bfbfbf"))
    drawer.line((60 + i * 90, 220, 120 + i * 90, 160), HEXtoRGB("#bfbfbf"))

for i, num in enumerate(numbers):
    if num == "0":
        drawer.rectangle((60 + i * 90, 100, 120 + i * 90, 220), outline=(0, 0, 0), width=3)
    elif num == "1":
        drawer.line((60 + i * 90, 160, 120 + i * 90, 100), (0, 0, 0), width=3)
        drawer.line((120 + i * 90, 100, 120 + i * 90, 220), (0, 0, 0), width=3)
    elif num == "2":
        drawer.line((60 + i * 90, 100, 120 + i * 90, 100), (0, 0, 0), width=3)
        drawer.line((120 + i * 90, 100, 120 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 220, 120 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 220, 120 + i * 90, 220), (0, 0, 0), width=3)
    elif num == "3":
        drawer.line((60 + i * 90, 100, 120 + i * 90, 100), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 160, 120 + i * 90, 100), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 160, 120 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 220, 120 + i * 90, 160), (0, 0, 0), width=3)
    elif num == "4":
        drawer.line((60 + i * 90, 100, 60 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 160, 120 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((120 + i * 90, 100, 120 + i * 90, 220), (0, 0, 0), width=3)
    elif num == "5":
        drawer.line((60 + i * 90, 100, 120 + i * 90, 100), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 100, 60 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 160, 120 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((120 + i * 90, 160, 120 + i * 90, 220), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 220, 120 + i * 90, 220), (0, 0, 0), width=3)
    elif num == "6":
        drawer.line((60 + i * 90, 160, 120 + i * 90, 100), (0, 0, 0), width=3)
        drawer.rectangle((60 + i * 90, 160, 120 + i * 90, 220), outline=(0, 0, 0), width=3)
    elif num == "7":
        drawer.line((60 + i * 90, 100, 120 + i * 90, 100), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 160, 120 + i * 90, 100), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 160, 60 + i * 90, 220), (0, 0, 0), width=3)
    elif num == "8":
        drawer.rectangle((60 + i * 90, 100, 120 + i * 90, 220), outline=(0, 0, 0), width=3)
        drawer.line((60 + i * 90, 160, 120 + i * 90, 160), (0, 0, 0), width=3)
    elif num == "9":
        drawer.line((60 + i * 90, 100, 120 + i * 90, 100), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 100, 60 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((120 + i * 90, 100, 120 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 160, 120 + i * 90, 160), (0, 0, 0), width=3)
        drawer.line((60 + i * 90, 220, 120 + i * 90, 160), (0, 0, 0), width=3)

image.save("index.png")
