from PIL import Image, ImageFilter


def motion_blur(n):
    img = Image.open("image.jpg")
    img_rotated = img.rotate(270, expand=True)
    img_blurred = img_rotated.filter(ImageFilter.GaussianBlur(n))
    img_blurred.save("res.jpg")
