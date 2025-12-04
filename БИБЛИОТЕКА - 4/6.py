from PIL import Image, ImageFilter

image = Image.open('picture.png')
reflection = image.transpose(Image.FLIP_TOP_BOTTOM)
blur_radius = float(input())

reflection_blurred = reflection.filter(ImageFilter.GaussianBlur(radius=blur_radius))
width, height = image.size
new_image = Image.new('RGB', (width, height * 2))
new_image.paste(image, (0, 0))
new_image.paste(reflection_blurred, (0, height))
new_image.save('result.png')
