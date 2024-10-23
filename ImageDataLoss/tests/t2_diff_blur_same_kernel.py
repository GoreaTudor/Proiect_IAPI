from tests import read_image, create_folder, box_blur, gaussian_blur, median_blur, write_image, IMG_FLOWER_1920


def diff_blur_same_kernel(image_path: str, ksize: int):
    img = read_image(image_path)
    folder = create_folder("T2")

    box = box_blur(img, ksize)
    gauss = gaussian_blur(img, ksize)
    median = median_blur(img, ksize)

    write_image(img, "original.jpeg", folder)
    write_image(box, f"box_{ksize}x{ksize}.jpeg", folder)
    write_image(gauss, f"gauss_{ksize}x{ksize}.jpeg", folder)
    write_image(median, f"median_{ksize}x{ksize}.jpeg", folder)


if __name__ == '__main__':
    diff_blur_same_kernel(image_path=IMG_FLOWER_1920,
                          ksize=11)
