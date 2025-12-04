from PIL import Image

desert = Image.open("desert.png")
camel = Image.open("camel.png")
if camel.mode != 'RGBA':
    camel = camel.convert('RGBA')
x, y = map(int, input().split())
reflect_input = input().strip()
if reflect_input == "reflect":
    camel = camel.transpose(Image.FLIP_LEFT_RIGHT)
camel_alpha = camel.split()[3]
desert.paste(camel, (x, y), camel_alpha)
desert.save("happy_camel.png")
