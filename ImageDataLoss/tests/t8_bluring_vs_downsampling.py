from tests import read_image, create_folder, write_image, box_blur, resize_image, BOOKSHELF_IMAGE


def blurring_vs_downscaling(image_path: str, ksize: int, size: int):
    image = read_image(image_path)
    folder = create_folder("T8")
    write_image(image, "original.jpeg", folder)

    blurred_image = box_blur(image, ksize)
    downsized_image = resize_image(image, size)

    write_image(blurred_image, "blurred.jpeg", folder)
    write_image(downsized_image, "downsized.jpeg", folder)


if __name__ == '__main__':
    blurring_vs_downscaling(image_path=BOOKSHELF_IMAGE,
                            ksize=11,
                            size=512)
