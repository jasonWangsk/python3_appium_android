#!usr/bin/env python3
# -*-coding:utf-8-*-

import time
import unittest
from config import appium_config
from testcase.sss_aa import element_cfg
from common.log import LOG,logger

@logger('appium--连nox夜神模拟器。。。')
class Mytest(unittest.TestCase):
    """封装unittest"""
    @classmethod
    def setUpClass(cls):
        # print("appium--连nox夜神模拟器。。。")
        cls.driver = appium_config.appium_start()
        cls.driver.implicitly_wait(8)

        cls.driver.find_element_by_id(element_cfg.get('login_page', '头像')).click()  # 点击头像进入个人中心
        time.sleep(1)
        cls.driver.find_element_by_id(element_cfg.get('login_page', '登录|注册')).click()  # 点击注册 进入登录页面


    # 测试结束后执行的方法
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()