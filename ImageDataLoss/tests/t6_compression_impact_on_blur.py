from typing import List

from tests import read_image, BOOKSHELF_IMAGE, write_image, create_folder, resize_image, box_blur


def compression_impact_on_blur(qualities: List[int], ksize: int):
    image = read_image(BOOKSHELF_IMAGE)
    folder_name = create_folder("T6")

    write_image(image, "original.jpeg", folder_name)

    blurred_image = box_blur(image, ksize)

    for quality in qualities:
        write_image(blurred_image, f"q_{quality}.jpeg", folder_name)

    write_image(blurred_image, "as_png.png", folder_name)


if __name__ == '__main__':
    compression_impact_on_blur(qualities=[90, 70, 50],
                               ksize=11)
