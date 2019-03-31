import pytesseract
from PIL import Image
import datetime
# todo:识别图片信息后存到本地

def main():
    for i in range(1, 2):
        starttime = datetime.datetime.now()
        image = Image.open(r"/Users/tester/project/android_autotest-master/screenshots/" + "201902231202.png")
        # image = Image.open(r"/Users/tester/project/android_autotest-master/screenshots/1122.png")
        text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
        endtime = datetime.datetime.now()

        print(r"计算机网络_" + str(i) + r"转换完成，耗时：" + str((endtime - starttime).seconds))

        text = text.replace(" ", "")
        with open(r"/Users/tester/project/android_autotest-master/" + str(i) + ".txt", "a") as f:  # 将识别出来的文字存到本地
            print(text)
            f.write(str(text))

if __name__ == '__main__':
    main()