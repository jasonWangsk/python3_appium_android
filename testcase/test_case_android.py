#!usr/bin/env python3
# -*-coding:utf-8-*-

import os
import time
import unittest
from lib2to3.pgen2 import driver
from config import appium_config
from appium.webdriver.common.touch_action import TouchAction

class android_88gongxiang(unittest.TestCase):
    """
    测试开始前执行的方法
    @classmethod,在此类中只进行一次初始化和清理工作
    """
    @classmethod
    def setUp(self):
        print("appium--连nox夜神模拟器。。。")
        self.driver = appium_config.appium_start()
        self.driver.implicitly_wait(8)
        self.driver.find_element_by_id("com.bx.chuxing:id/a3j").click() # 进入个人中心
        time.sleep(2)


    def test_appcase_0(self):
        """环境切换"""
        try:
            time.sleep(2)
            print('clickg-关于我们')
            self.driver.find_element_by_id("com.bx.chuxing:id/pn").click()
            time.sleep(2)
            print('press--短按 关于我们切换环境地址。。。')
            self.driver.long_press_keycode("com.bx.chuxing:id/os")
            action = TouchAction(driver)
            action.long_press(self.driver.find_element_by_id("com.bx.chuxing:id/os"),3000).perform()
            # 切换环境地址
            time.sleep(2)
            self.driver.find_element_by_id("com.bx.chuxing:id/rz").click()
            print("测试通过。。。")
        except  RuntimeError:
            self.driver.close()
            pass

        # except (Exception) as Argument:
        #     print("测试失败",Argument)


    # def test_appcase_1(self):
    #     """首页-点击头像跳转到登录页面"""
    #     try:
    #         time.sleep(2)
    #         self.driver.find_element_by_id("com.bx.chuxing:id/cv").click()
    #         time.sleep(4)
    #         # self.driver.find_element_by_id("com.bx.chuxing:id/qc").send_keys("15902198009")
    #         # time.sleep(1)
    #
    #         # 截屏
    #         # image_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) + "//screenshots//"
    #         # time_format = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    #         # screen_save_path = image_folder + time_format + '.png'
    #         # self.driver.get_screenshot_as_file(screen_save_path)
    #         # #
    #         # # time.sleep(5)
    #         # self.driver.find_element_by_id("com.bx.chuxing:id/a20").send_keys("22fg")
    #         # time.sleep(1)
    #         # self.driver.find_element_by_id("com.bx.chuxing:id/a27").send_keys("489703")
    #         #
    #         # time.sleep(1)
    #         # self.driver.find_element_by_id("com.bx.chuxing:id/a25").click()
    #         # time.sleep(1)
    #         # self.driver.find_element_by_id("com.bx.chuxing:id/a1x").click()
    #         # time.sleep(1)
    #         # driver.find_element_by_id("com.bx.chuxing:id/bf").click()
    #         time.sleep(5)
    #         print("测试通过")
    #     except False:
    #         return False

    def test_appcase_2(self):
        """手机号码长度大于11位-点击登录"""
        self.driver.find_element_by_id("com.bx.chuxing:id/cv").click() # 进入登录页面
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/qc").send_keys("123456789012")
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a1x").click() # 点击登录
        time.sleep(2)
        print("测试通过")

    def test_appcase_3(self):
        """手机号码非法-点击登录"""
        self.driver.find_element_by_id("com.bx.chuxing:id/cv").click() # 进入登录页面
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/qc").send_keys("123")
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a1x").click() # 点击登录
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/qc").clear() # 清空
        print("测试通过")

    def test_appcase_4(self):
        """图片验证码长度非法-登录"""
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/cv").click() # 进入登录页面
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a20").send_keys("1234567")
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a1x").click() # 点击登录
        time.sleep(2)
        print("测试通过")

    def test_appcase_5(self):
        """短信验证码非法-登录"""
        self.driver.find_element_by_id("com.bx.chuxing:id/cv").click() # 进入登录页面
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a27").send_keys("12！@")
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a1x").click()  # 点击登录
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a27").clear()  # 清空
        print("测试通过")
    def test_appcase_6(self):
        """登录页面输入所有要素"""
        self.driver.find_element_by_id("com.bx.chuxing:id/cv").click()  # 进入登录页面
        time.sleep(2)
        # 截屏
        image_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "//screenshots//"
        time_format = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = image_folder + time_format + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/qc").send_keys("15902198009")
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a20").send_keys("0703")   # 图片验证码
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a27").send_keys("489703")   # 短信验证码
        time.sleep(2)
        self.driver.find_element_by_id("com.bx.chuxing:id/a25").click()  # 同意平台
        time.sleep(2)
        message_title = self.driver.find_element_by_id("com.bx.chuxing:id/a1x").text
        print("获取title-进行断言:",message_title)
        self.assertEqual(message_title,'登录')
        # 点击登录
        self.driver.find_element_by_id("com.bx.chuxing:id/a1x").click()

        print("测试通过")
        time.sleep(20)



    # 测试结束后执行的方法
    @classmethod
    def tearDownClass(self):

        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
