import cv2
import os
import datetime
import numpy as np

E_MC2_IMAGE = "..\\assets\\pexels-jeshoots-com-147458-714699.jpg"
DICE_IMAGE = "..\\assets\\pexels-pixabay-37534.jpg"
BOOKSHELF_IMAGE = "..\\assets\\pexels-rachel-claire-5490916.jpg"


##### OS #####

def create_folder(prefix: str = "test"):
    timestamp = datetime.datetime.now().strftime("%y-%m-%d__%H-%M-%S")
    folder_name = f"{prefix}__{timestamp}"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return folder_name


def read_image(path):
    image = cv2.imread(path)

    if image is None:
        print("Error: Could not load image")
        return None

    return image


def write_image(image, file_name: str, folder_name: str):
    path = os.path.join(folder_name, file_name)
    cv2.imwrite(path, image)


def write_image_with_quality(image, file_name: str, folder_name: str, quality: int):
    path = os.path.join(folder_name, file_name)
    cv2.imwrite(path, image, [cv2.IMWRITE_JPEG_QUALITY, quality])


##### UTILS #####

def resize_image(image, size: int):
    return cv2.resize(image, (size, size))


def split_image_color_channels(image):
    return cv2.split(image)


def merge_image_color_channels(channels):
    return cv2.merge(channels)


def add_noise_to_image(image):
    noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
    return cv2.add(image, noise)


##### BLURS #####

def gaussian_blur(image, kernel_size: int):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


def box_blur(image, kernel_size: int):
    return cv2.blur(image, (kernel_size, kernel_size))


def median_blur(image, kernel_size: int):
    return cv2.medianBlur(image, kernel_size)


# todo:
# - add bilateral blur
# - add motion blur (with diff kernels: vertical, horizontal, ...)
# - test: blur chaining, ???


BLURS = {
    "box": box_blur,
    "median": median_blur,
    "gaussian": gaussian_blur,
}
