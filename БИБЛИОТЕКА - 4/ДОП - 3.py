from PIL import Image, ImageFilter

forest = Image.open("../forest.png")
hedgehog = Image.open("../hedgehog.png")
hedgehog = hedgehog.resize(
    (hedgehog.width // 2, hedgehog.height // 2),
    Image.Resampling.NEAREST
)

x_coordinate = int(input())
forest_height = forest.height
hedgehog_height = hedgehog.height
forest_copy = forest.copy()
forest_copy.paste(hedgehog, (x_coordinate, forest_height - hedgehog_height))
forest_copy = forest_copy.filter(ImageFilter.BLUR)

forest_copy.save("hedgehog_in_fog.png")
