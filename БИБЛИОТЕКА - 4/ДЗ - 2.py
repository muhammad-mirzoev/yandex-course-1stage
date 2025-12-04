from PIL import Image

tree_img = Image.open("tree.png")
tree_crop = tree_img.crop((50, 50, 450, 450))
gray_value = int(input())
tree_gray = tree_crop.convert("L").point(lambda p: gray_value if p > 0 else 0)
tree_gray_rotated = tree_gray.transpose(Image.ROTATE_90).resize((int(tree_gray.width * 0.5), tree_gray.height))
shadow_img = Image.new("RGBA", (tree_gray_rotated.width, tree_gray_rotated.height), (0, 0, 0, 0))
shadow_img.paste(tree_gray_rotated, (300, 400 - tree_gray_rotated.height), tree_gray_rotated)
shadow_img.save("shadow.png")
