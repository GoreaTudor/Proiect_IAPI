from tests import read_image, create_folder, write_image, add_noise_to_image, gaussian_blur, IMG_BOOKSHELF


def noise_reduction(image_path: str, ksize: int):
    image = read_image(image_path)
    folder = create_folder("T9")
    write_image(image, "original.jpeg", folder)

    noisy_image = add_noise_to_image(image)
    blurred_image = gaussian_blur(noisy_image, ksize)

    write_image(noisy_image, "noisy.jpeg", folder)
    write_image(blurred_image, "noise_reduced.jpeg", folder)


if __name__ == '__main__':
    noise_reduction(image_path=IMG_BOOKSHELF,
                    ksize=11)
