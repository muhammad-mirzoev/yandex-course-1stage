from PIL import Image, ImageDraw


class Drawer:
    def __init__(self, draw_map, cell_size=20):
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.color_map = {}

    def numbers(self):
        unique_numbers = set()
        for row in self.draw_map:
            unique_numbers.update(row)
        return sorted(unique_numbers)

    def set_color(self, number, color):
        self.color_map[number] = color

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        height = len(self.draw_map)
        width = len(self.draw_map[0])
        return (width * self.cell_size, height * self.cell_size)

    def draw(self):
        width, height = self.size()
        image = Image.new("RGB", (width, height), "white")  # Белый фон
        draw = ImageDraw.Draw(image)
        for y, row in enumerate(self.draw_map):
            for x, number in enumerate(row):
                color = self.color_map.get(number, "black")
                top_left = (x * self.cell_size, y * self.cell_size)
                bottom_right = ((x + 1) * self.cell_size, (y + 1) * self.cell_size)
                draw.rectangle([top_left, bottom_right], fill=color)

        return image
