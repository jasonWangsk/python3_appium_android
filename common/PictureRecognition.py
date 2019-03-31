#coding:utf8
import os
from PIL import Image
import pytesseract
# todo:图片识别


# file=r"/Users/tester/project/android_autotest-master/screenshots/QQ.JPG"
file = r"QQ.jpg"
# # file=r"D:\work\python36_crawl\pictureParser\英文.png"
if os.path.exists(file):
    image = Image.open(file)
    # 英文
    # vcode = pytesseract.image_to_string(image,"eng")
    # vcode = pytesseract.image_to_string(image,lang='chi_sim')
    text = pytesseract.image_to_string(image)

    print(text)