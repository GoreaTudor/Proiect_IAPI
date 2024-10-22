from tests import read_image, create_folder, write_image, BLURS, IMG_BOOKSHELF


def same_blur_diff_kernel(image_path: str, blur: str, ksize_min: int, ksize_max: int):
    img = read_image(image_path)
    folder = create_folder("T3")
    write_image(img, "original.jpeg", folder)

    for ksize in range(ksize_min, ksize_max + 1, 2):
        blurred_img = BLURS[blur](img, ksize)
        write_image(blurred_img, f"{blur}_{ksize}x{ksize}.jpeg", folder)


if __name__ == '__main__':
    same_blur_diff_kernel(image_path=IMG_BOOKSHELF,
                          blur="box",
                          ksize_min=3,
                          ksize_max=11)
