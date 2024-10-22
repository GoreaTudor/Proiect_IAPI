from typing import List

from tests import read_image, BOOKSHELF_IMAGE, write_image, create_folder, split_image_color_channels, box_blur, \
    merge_image_color_channels


def blurring_color_channels(sizes: List[int], ksize: int):
    image = read_image(BOOKSHELF_IMAGE)  # todo many color regions
    folder_name = create_folder("T5")

    write_image(image, "original.jpeg", folder_name)

    blue_ch, green_ch, red_ch = split_image_color_channels(image)

    blurred_blue_ch = box_blur(blue_ch, ksize)
    blurred_green_ch = box_blur(green_ch, ksize)
    blurred_red_ch = box_blur(red_ch, ksize)

    blurred_img_simple = box_blur(image, ksize)
    blurred_img_channels = merge_image_color_channels([blurred_blue_ch, blurred_green_ch, blurred_red_ch])

    write_image(blurred_img_simple, f"blurred_simple.jpeg", folder_name)
    write_image(blurred_img_channels, f"blurred_channels.jpeg", folder_name)


if __name__ == '__main__':
    blurring_color_channels(sizes=[512, 1024, 2048],
                            ksize=11)
