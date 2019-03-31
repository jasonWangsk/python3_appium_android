#!usr/bin/env python3
# -*-coding:utf-8-*-
# todo:封装appium连接夜神模拟器函数
import time
from config import appium_server
from appium import webdriver

time.sleep(2)
print("启动/关闭appium--server",'\n')
stop_appiumServer = appium_server.stop_appium()
time.sleep(2)
start_appiumServer = appium_server.start_appium()
# 测试开始前执行的方法
def appium_start():
    desired_caps = {'platformName': 'Android',  # 平台名称
                    'platformVersion': '4.4.2',  # 系统版本号
                    'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                    'appPackage': 'com.baixiang.chuxing',  # apk的包名
                    'appActivity': 'com.baixiang.chuxing.activity.SplashActivity',  # activity 名称
                    'unicodeKeyboard':True  # 编码,可解决中文输入问题

    }

    return  webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
