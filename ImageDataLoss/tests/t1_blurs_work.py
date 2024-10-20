import cv2

from tests import BOOKSHELF_IMAGE


def resize_image(image, max_width=800, max_height=600):
    """Resize the image to fit within the specified dimensions, maintaining aspect ratio."""
    height, width = image.shape[:2]

    aspect_ratio = width / height

    if width > max_width:
        width = max_width
        height = int(width / aspect_ratio)

    if height > max_height:
        height = max_height
        width = int(height * aspect_ratio)

    return cv2.resize(image, (width, height))

# I did this test bc. the burring didn't seem to work...
# It does work, just not the way I expected
if __name__ == '__main__':
    image = cv2.imread(BOOKSHELF_IMAGE)
    resized_image = resize_image(image)

    # apparently the blur was applied, but a bigger kernel was needed to distinguish with eyes
    blurred_image = cv2.blur(resized_image, (5, 5), 0)

    cv2.imshow("Original Image", resized_image)
    cv2.imshow("Blurred Image 1", blurred_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
