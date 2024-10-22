from tests import read_image, create_folder, write_image, split_image_color_channels, box_blur, \
    merge_image_color_channels, IMG_BOOKSHELF


def blurring_color_channels(image_path: str, ksize: int):
    image = read_image(image_path)
    folder = create_folder("T5")
    write_image(image, "original.jpeg", folder)

    blue_ch, green_ch, red_ch = split_image_color_channels(image)

    blurred_blue_ch = box_blur(blue_ch, ksize)
    blurred_green_ch = box_blur(green_ch, ksize)
    blurred_red_ch = box_blur(red_ch, ksize)

    blurred_img_simple = box_blur(image, ksize)
    blurred_img_channels = merge_image_color_channels([blurred_blue_ch, blurred_green_ch, blurred_red_ch])

    write_image(blurred_img_simple, f"blurred_simple.jpeg", folder)
    write_image(blurred_img_channels, f"blurred_channels.jpeg", folder)


if __name__ == '__main__':
    blurring_color_channels(image_path=IMG_BOOKSHELF,  # todo many color regions
                            ksize=11)
