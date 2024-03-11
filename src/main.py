"""
App short description:
The app will be accepting images of receipts that the user will be sending over, scan the information to ensure image
clarity and usefulness of the content on the receipt, and when the content is deemed satisfactory, award the user with
a tiny sum of money for each receipt.

Quality assurance:
The data must contain information such as product bought, quantity, price, company (seller), geographical location,
along with user data such as age and sex which will be provided via the user account during the account creation.

Business case:
The business model is that the user is getting paid by our startup company for images of receipts, which in turn is
sold to data processors as consumer data information or market trends. The incentive for the user will be to submit a
large number of receipts which can amount to a decent total sum, while for the company will be to understand the types
of data that are attractive to data processor companies.

Business need:
Further research is required to determine how data about trends is collected by companies, and the general market chain
for data gathering and processing of consumer information.

Future plans:
In the future, our company may or may not perform in-house data analysis, but initially will only sell the raw data in
bulk.


"""

import pytesseract
from PIL import Image
import cv2


def main():

    file_name = 'image_sample3.jpg'

    # using pillow
    pillow_image = Image.open(file_name)
    # data = pytesseract.image_to_data(pillow_image, timeout=10)
    text = pytesseract.image_to_string(pillow_image, timeout=10)
    print('-' * 45, '\nPILLOW lib\n\n', text)

    # using opencv
    cv_image = cv2.imread(file_name)
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    print('-' * 45, '\nOPENCV lib\n\n', text)


if __name__ == '__main__':
    main()
