import cv2

from tests import IMG_FLOWER_640, IMG_FLOWER_1280, IMG_FLOWER_1920, resize_image

if __name__ == '__main__':
    image_640 = cv2.imread(IMG_FLOWER_640)
    image_1280 = cv2.imread(IMG_FLOWER_1280)
    image_1920 = cv2.imread(IMG_FLOWER_1920)

    blurred_image_640 = cv2.blur(image_640, (5, 5), 0)
    blurred_image_1280 = cv2.blur(image_1280, (5, 5), 0)
    blurred_image_1920 = cv2.blur(image_1920, (5, 5), 0)

    cv2.imshow("Original Image (640)", image_640)
    cv2.imshow("Blurred Image (640)", blurred_image_640)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow("Original Image (1280)", resize_image(image_1280, 640, 360))
    cv2.imshow("Blurred Image (1280)", resize_image(blurred_image_1280, 640, 360))
    # cv2.imshow("Original Image (1280)", image_1280)
    # cv2.imshow("Blurred Image (1280)", blurred_image_1280)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow("Original Image (1920)", resize_image(image_1920, 640, 360))
    cv2.imshow("Blurred Image (1920)", resize_image(blurred_image_1920, 640, 360))
    # cv2.imshow("Original Image (1920)", image_1920)
    # cv2.imshow("Blurred Image (1920)", blurred_image_1920)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
