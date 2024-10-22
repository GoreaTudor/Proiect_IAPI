from typing import List

from tests import read_image, create_folder, write_image, BLURS, BOOKSHELF_IMAGE


def chained_blurs(image_path: str, blurs: List[str], ksize: int):
    image = read_image(image_path)
    folder = create_folder("T7")
    write_image(image, "original.jpeg", folder)

    it = 0
    blurred_image = image

    for blur in blurs:
        blurred_image = BLURS[blur](blurred_image, ksize)
        it += 1
        write_image(blurred_image, f"blur_{it}_{blur}.jpeg", folder)


if __name__ == '__main__':
    chained_blurs(image_path=BOOKSHELF_IMAGE,
                  blurs=["box", "box", "median", "gaussian"],
                  ksize=11)
