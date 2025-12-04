from PIL import Image


def twist_image(input_file_name, output_file_name):
    image = Image.open(input_file_name)
    width, height = image.size

    left_half = image.crop((0, 0, width // 2, height))
    right_half = image.crop((width // 2, 0, width, height))

    new_image = Image.new("RGB", (width, height))
    new_image.paste(right_half, (0, 0))
    new_image.paste(left_half, (width // 2, 0))

    new_image.save(output_file_name)
