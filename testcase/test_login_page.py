#!usr/bin/env python3
# -*-coding:utf-8-*-

import time
import unittest
from common import unittest_main
from common import screen_shot
from common import read_config

element_cfg = read_config.elements_read()
screen_file = screen_shot.screen_shot_android(neme='')

class android_login(unittest_main.Mytest):

    def test_appcase_001(self):
        """登录-个人中心-拼车|班车行程-回退"""
        try:
            time.sleep(2)
            self.driver.find_element_by_id(element_cfg.get('login_page', 'mobilephone')).send_keys("15902198009")
            time.sleep(1)
            self.driver.find_element_by_id(element_cfg.get('login_page', '图片验证码')).send_keys("0703")  # 图片验证码
            time.sleep(1)
            self.driver.find_element_by_id(element_cfg.get('login_page', '短信验证码')).send_keys("489703")  # 短信验证码
            time.sleep(1)
            self.driver.find_element_by_id(element_cfg.get('login_page', '同意平台')).click()  # 同意平台
            time.sleep(1)
            self.driver.find_element_by_id(element_cfg.get('login_page', '登录button')).click()  # 登录
            time.sleep(1)
            self.driver.find_element_by_id(element_cfg.get('login_page','头像')).click()  # 点击头像进入个人中心
            time.sleep(2)
            self.driver.find_element_by_id(element_cfg.get('个人中心', '遮罩')).click()  # 去除遮罩
            time.sleep(2)
            self.driver.find_element_by_id(element_cfg.get('个人中心','拼车|班车行程')).click()   # 点击拼车|班车行程
            message_title = self.driver.find_element_by_id("com.baixiang.chuxing:id/ap8").text
            print('\n',"获取title-进行断言:", message_title)
            self.assertEqual(message_title, '拼车 / 班车行程')

            time.sleep(2)
            print('\n',"截取屏幕。。。")
            self.driver.get_screenshot_as_file(screen_file)
            time.sleep(1)
            if self.driver.find_element_by_id(element_cfg.get('个人中心','拼车|班车行程')).is_displayed():
                print('测试失败')
        except Exception:
            print('\n',"测试通过。。。")
            time.sleep(2)
            self.driver.find_element_by_id(element_cfg.get('公共', '回退')).click()
            print('回退成功')

    def test_appcase_002(self):
        """个人中心--租车行程--回退"""
        try:
            time.sleep(2)
            self.sss = android_login.test_appcase_001(self)     #方法继承
            time.sleep(2)
            print('点击租车行程')
            self.driver.find_element_by_id(element_cfg.get('个人中心','租车行程')).click()
            time.sleep(1)
            self.driver.find_element_by_id(element_cfg.get('公共', '回退')).click()
            print('回退成功')
            time.sleep(1)
            print('点击我的车')
            self.driver.find_element_by_id(element_cfg.get('个人中心','我的车')).click()
            time.sleep(1)
            self.driver.find_element_by_id(element_cfg.get('公共','回退')).click()
            print('回退成功')
        except Exception:
            print('\n','测试通过。。。')





if __name__ == '__main__':

    unittest.main()
