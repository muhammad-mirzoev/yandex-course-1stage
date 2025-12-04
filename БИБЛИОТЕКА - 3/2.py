from PIL import Image

image = Image.open('../image.jpg')

w, h = image.size
rr, gg, bb = 0, 0, 0

for x in range(w):
    for y in range(h):
        r, g, b = image.getpixel((x, y))
        rr += r
        gg += g
        bb += b

cnt = w * h
print(rr // cnt, gg // cnt, bb // cnt)
