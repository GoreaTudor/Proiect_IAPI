from typing import List, Tuple

from tests import read_image, BOOKSHELF_IMAGE, write_image, create_folder, resize_image, box_blur, BLURS


def blurring_vs_downscaling(ksize: int, size: int):
    image = read_image(BOOKSHELF_IMAGE)
    folder_name = create_folder("T8")

    write_image(image, "original.jpeg", folder_name)

    blurred_image = box_blur(image, ksize)
    downsized_image = resize_image(image, size)

    write_image(blurred_image, "blurred.jpeg", folder_name)
    write_image(downsized_image, "downsized.jpeg", folder_name)


if __name__ == '__main__':
    blurring_vs_downscaling(ksize=11,
                            size=512)
