from typing import List

from tests import read_image, write_image, create_folder, resize_image, BLURS, IMG_FLOWER_1920


def blur_diff_img_sizes(image_path: str, blur: str, sizes: List[int], ksize: int):
    image = read_image(image_path)
    folder = create_folder("T4")
    write_image(image, "original.jpeg", folder)

    for size in sizes:
        resized_image = resize_image(image, size, size)
        blurred_image = BLURS[blur](resized_image, ksize)

        write_image(blurred_image, f"{blur}_{ksize}__on_{size}.jpeg", folder)


if __name__ == '__main__':
    blur_diff_img_sizes(image_path=IMG_FLOWER_1920,
                        blur="median",
                        sizes=[512, 1024, 2048],
                        ksize=11)
