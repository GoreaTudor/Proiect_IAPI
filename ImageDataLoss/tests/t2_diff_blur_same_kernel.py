from tests import BOOKSHELF_IMAGE
from tests import box_blur, gaussian_blur, median_blur
from tests import create_folder, read_image, write_image

def diff_blur_same_kernel(image_path, ksize):
    img = read_image(image_path)
    folder_name = create_folder("T2")

    box = box_blur(img, ksize)
    gauss = gaussian_blur(img, ksize)
    median = median_blur(img, ksize)

    write_image(img, "original.jpeg", folder_name)
    write_image(box, f"median_{ksize}x{ksize}.jpeg", folder_name)
    write_image(gauss, f"gauss_{ksize}x{ksize}.jpeg", folder_name)
    write_image(median, f"median_{ksize}x{ksize}.jpeg", folder_name)

    print(f"Blurred images saved in: {folder_name}")


if __name__ == '__main__':
    diff_blur_same_kernel(image_path=BOOKSHELF_IMAGE,
                          ksize=11)
