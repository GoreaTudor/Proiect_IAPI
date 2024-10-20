import cv2
from PIL import Image


##### BLURRING #####


def apply_gaussian_blur(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def apply_box_blur(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

def apply_median_blur(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)


#### COMPRESSION #####


def compress_image(image_path, output_path, format, quality=90):
    image = Image.open(image_path)
    image.save(output_path, format=format, quality=quality)

def convert_bgr_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
