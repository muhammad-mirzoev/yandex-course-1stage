from PIL import Image


def rotate_image(input_image_path, output_image_path, angle, new_background_color):
    image = Image.open(input_image_path)
    rotated_image = image.rotate(angle, expand=True, fillcolor=new_background_color)
    rotated_image.save(output_image_path)


angle = float(input())
new_background_color = tuple(map(int, input().split(',')))
rotate_image('sunflower.png', 'turned_sunflower.png', angle, new_background_color)
