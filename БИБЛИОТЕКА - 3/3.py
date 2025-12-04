from PIL import Image

def mirror():
    img = Image.open('image.jpg')

    mirrored_img = img.transpose(Image.FLIP_LEFT_RIGHT)

    mirrored_img.save('res.jpg')

mirror()
