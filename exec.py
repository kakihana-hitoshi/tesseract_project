import pytesseract
from PIL import Image
import sys

args = sys.argv
image = 'google-docu.jpg'
if 2 <= len(args):
    image = args[1]

# 日本語
str_jp_img = Image.open(image)
str_jp = pytesseract.image_to_string(str_jp_img, lang="jpn")
print(str_jp)

# 英語　デフォルト
# str_img = Image.open(image)
# str = pytesseract.image_to_string(str_img)
# print(str)