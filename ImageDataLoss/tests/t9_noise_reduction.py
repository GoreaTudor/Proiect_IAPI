from typing import List, Tuple

from tests import read_image, BOOKSHELF_IMAGE, write_image, create_folder, resize_image, box_blur, BLURS, gaussian_blur, \
    add_noise_to_image


def noise_reduction(ksize: int):
    image = read_image(BOOKSHELF_IMAGE)
    folder_name = create_folder("T9")

    write_image(image, "original.jpeg", folder_name)

    noisy_image = add_noise_to_image(image)
    blurred_image = gaussian_blur(image, ksize)

    write_image(noisy_image, "noisy.jpeg", folder_name)
    write_image(blurred_image, "noise_reduced.jpeg", folder_name)


if __name__ == '__main__':
    noise_reduction(ksize=11)
