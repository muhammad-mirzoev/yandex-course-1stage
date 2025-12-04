from PIL import Image, ImageOps


def add_border(image_path, border_thickness, border_color, output_path):
    image = Image.open(image_path)
    bordered_image = ImageOps.expand(image, border=border_thickness, fill=border_color)
    bordered_image.save(output_path)


image_path = "portrait.png"
output_path = "border.png"
border_thickness = 20
border_color = "#c647d1"

add_border(image_path, border_thickness, border_color, output_path)
