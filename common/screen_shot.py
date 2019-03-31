#！usr/bin/env python3
# -*-coding:utf-8-*-
import os
import time
def screen_shot_android(neme):
    """
    截屏
    :return:
    """
    image_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "//screenshots//login_page//"
    time_format = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screen_save_path = image_folder + (f'{neme}') +time_format + '.png'    # 截屏存放路径
    return  screen_save_path

screen_shot_android('login')
