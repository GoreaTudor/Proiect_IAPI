from typing import List

from tests import read_image, BOOKSHELF_IMAGE, write_image, create_folder, resize_image, box_blur, BLURS


def chained_blurs(blurs: List[str], ksize: int):
    image = read_image(BOOKSHELF_IMAGE)
    folder_name = create_folder("T7")

    write_image(image, "original.jpeg", folder_name)

    it = 0
    blurred_image = image

    for blur in blurs:
        blurred_image = BLURS[blur](blurred_image, ksize)
        it += 1
        write_image(blurred_image, f"blur_{it}_{blur}.jpeg", folder_name)


if __name__ == '__main__':
    chained_blurs(blurs=["box", "box", "median", "gaussian"],
                  ksize=11)
