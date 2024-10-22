from typing import List

from tests import read_image, create_folder, write_image, box_blur, write_image_with_quality, IMG_BOOKSHELF


def compression_impact_on_blur(image_path: str, qualities: List[int], ksize: int):
    image = read_image(image_path)
    folder = create_folder("T6")
    write_image(image, "original.jpeg", folder)

    blurred_image = box_blur(image, ksize)

    for quality in qualities:
        write_image_with_quality(blurred_image, f"q_{quality}.jpeg", folder, quality)

    write_image(blurred_image, "as_png.png", folder)


if __name__ == '__main__':
    compression_impact_on_blur(image_path=IMG_BOOKSHELF,
                               qualities=[90, 70, 50],
                               ksize=11)
