import numpy as np
import pytesseract
from PIL import Image
import cv2


def main():

    file_name = 'image_sample3.jpg'

    # using pillow
    pillow_image = Image.open(file_name)
    # data = pytesseract.image_to_data(pillow_image, timeout=10)
    text = pytesseract.image_to_string(pillow_image, timeout=10)
    # print('-' * 45, '\nPILLOW lib\n\n', text)

    # using opencv
    cv_image = cv2.imread(file_name)

    # turn to greyscale
    grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    # Gaussian blur to remove some noise
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    bin_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Perform dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(bin_img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # text = pytesseract.image_to_string(img)
    # text = cv2.haveImageReader(file_name)
    print('-' * 45, '\nOPENCV lib\n\n', text)


if __name__ == '__main__':
    main()
