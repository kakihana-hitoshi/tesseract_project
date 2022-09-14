import pytesseract
from PIL import Image

# 日本語
str_jp_img = Image.open('google-docu.jpg')
str_jp = pytesseract.image_to_string(str_jp_img, lang="jpn")
print(str_jp)

# 英語　デフォルト
# str_img = Image.open('google-docu.jpg')
# str = pytesseract.image_to_string(str_img)
# print(str)