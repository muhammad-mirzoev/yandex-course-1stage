from PIL import Image


def transparency(filename1, filename2):
    img1 = Image.open(filename1)
    img2 = Image.open(filename2)
    img1 = img1.resize(img2.size)
    pixels1 = img1.load()
    pixels2 = img2.load()

    result_img = Image.new('RGB', img1.size)
    result_pixels = result_img.load()
    for i in range(img1.width):
        for j in range(img1.height):
            r1, g1, b1 = pixels1[i, j]
            r2, g2, b2 = pixels2[i, j]

            r = int(0.5 * r1 + 0.5 * r2)
            g = int(0.5 * g1 + 0.5 * g2)
            b = int(0.5 * b1 + 0.5 * b2)
            result_pixels[i, j] = (r, g, b)

    result_img.save("res.jpg")
