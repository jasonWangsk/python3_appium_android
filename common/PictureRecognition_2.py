#!usr/bin/env python3
# coding:utf-8
from PIL import Image
from PIL import ImageEnhance
import pytesseract

im=Image.open("QQ.jpg")
im=im.convert('L')
im.show()
im=ImageEnhance.Contrast(im)
im=im.enhance(3)
im.show()
print(pytesseract.image_to_string(im))
