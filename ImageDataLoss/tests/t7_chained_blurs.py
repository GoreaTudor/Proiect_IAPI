from typing import List

from tests import read_image, create_folder, write_image, BLURS, IMG_FLOWER_1920, IMG_BOOKSHELF, IMG_MARKET


def chained_blurs(image_path: str, blurs: List[str], ksize: int):
    image = read_image(image_path)
    folder = create_folder("T7")
    write_image(image, "original.jpeg", folder)

    it = 0
    blurred_image = image

    for blur in blurs:
        blurred_image = BLURS[blur](blurred_image, ksize)
        it += 1
        if it % 10 == 0:
            write_image(blurred_image, f"blur_{it}_{blur}.jpeg", folder)


if __name__ == '__main__':
    chained_blurs(image_path=IMG_MARKET,
                  # blurs=["box", "box", "median", "gaussian"],
                  blurs=["box" for i in range(0, 100)],
                  ksize=3)
