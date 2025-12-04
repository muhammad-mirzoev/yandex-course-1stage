from PIL import Image


def split_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    part_width = width // 2
    part_height = height // 2
    parts = [
        img.crop((0, 0, part_width, part_height)),
        img.crop((part_width, 0, width, part_height)),
        img.crop((0, part_height, part_width, height)),
        img.crop((part_width, part_height, width, height))
    ]
    return parts


def rearrange_image(parts, order):
    new_image = Image.new('RGB', (parts[0].width * 2, parts[0].height * 2))
    new_image.paste(parts[order[0] - 1], (0, 0))
    new_image.paste(parts[order[1] - 1], (parts[0].width, 0))
    new_image.paste(parts[order[2] - 1], (0, parts[0].height))
    new_image.paste(parts[order[3] - 1], (parts[0].width, parts[0].height))
    return new_image


def main(image_path, order_str, output_path):
    parts = split_image(image_path)
    order = [int(digit) for digit in order_str]
    result_image = rearrange_image(parts, order)
    result_image.save(output_path)


image_path = "fruits.png"
order_str = "1243"
output_path = "cycle.png"

main(image_path, order_str, output_path)
