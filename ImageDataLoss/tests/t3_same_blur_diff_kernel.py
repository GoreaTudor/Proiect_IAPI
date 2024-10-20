from tests import BOOKSHELF_IMAGE, BLURS
from tests import create_folder, read_image, write_image

def same_blur_diff_kernel(image_path, blur: str, ksize_min: int, ksize_max: int):
    img = read_image(image_path)
    folder_name = create_folder("T3")

    write_image(img, "original.jpeg", folder_name)

    for ksize in range(ksize_min, ksize_max + 1, 2):
        blurred_img = BLURS[blur](img, ksize)
        write_image(blurred_img, f"{blur}_{ksize}x{ksize}.jpeg", folder_name)

    print(f"Blurred images saved in: {folder_name}")


if __name__ == '__main__':
    same_blur_diff_kernel(image_path=BOOKSHELF_IMAGE,
                          blur="box",
                          ksize_min=3,
                          ksize_max=11)
