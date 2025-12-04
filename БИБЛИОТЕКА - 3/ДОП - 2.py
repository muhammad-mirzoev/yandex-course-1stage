from PIL import Image
import numpy as np


def mix_images(bird_path, dino_path, coeff):
    bird = Image.open(bird_path)
    dino = Image.open(dino_path)
    bird_np = np.array(bird)
    dino_np = np.array(dino)

    if bird_np.shape != dino_np.shape:
        raise ValueError()

    result_np = np.clip(coeff * bird_np + (1 - coeff) * dino_np, 0, 255).astype(np.uint8)
    result_image = Image.fromarray(result_np)
    result_image.save('origin.png')


mix_images('bird.png', 'dino.png', 0.8)
