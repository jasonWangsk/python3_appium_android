# 导入相关的库
from PIL import Image, ImageEnhance
from pytesseract import pytesseract

import os


# todo：截取图片后裁剪尺寸-识别

def cut_image(text):

	file=r"/Users/tester/project/android_autotest-master/screenshots/201902232111.png"

	# 打开一张图
	img = Image.open(file)
	# 图片尺寸
	img_size = img.size
	h = img_size[1]  # 图片高度
	w = img_size[0]  # 图片宽度

	x = 0.47 * w
	y = 0.41 * h   # 上
	w = 0.31 * w   # 图片右侧宽度
	h = 0.044 * h   # 图片下面高度

	# 开始截取
	region = img.crop((x, y, x + w, y + h))
	# 保存图片
	region.save("/Users/tester/project/android_autotest-master/screenshots/test.png")
	# region.show()
	image = Image.open('/Users/tester/project/android_autotest-master/screenshots/test.png')
	# 转化为灰度图
	imgry = image.convert('L')
	# imgry.show()
	imgry.save("/Users/tester/project/android_autotest-master/screenshots/test2.png")
	# 二值化处理
	img2 = imgry.point(lambda x:255 if x>129 else 0)
	# img2.show()
	img2.save("/Users/tester/project/android_autotest-master/screenshots/test3.png")

	# sharpness = ImageEnhance.Contrast(img2)  # 对比度增强
	# i3 = sharpness.enhance(3.0)  # 3.0为图像的饱和度
	# i3.save("/Users/tester/project/android_autotest-master/screenshots/test4.png")
	# i4 = Image.open("/Users/tester/project/android_autotest-master/screenshots/test4.png")
    # 

	text = pytesseract.image_to_string(img2)
	print('二值处理后验证码识别：',text)
	# 去除数字以外的其他字符
	fil = filter(str.isdigit, text)
	new_text = ''
	for i in fil:
		new_text += i
	print('去除干扰后验证码识别：',new_text)
	return text
cut_image(text='text')