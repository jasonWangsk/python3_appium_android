#！usr/bin/env python3
# -*-coding:utf-8-*-
# 主函数

import os
import time
import unittest

from common.HTMLTestRunner import HTMLTestRunner

test_dir = './testcase'
discover = unittest.defaultTestLoader.discover(start_dir='./testcase', pattern="test_login_page.py")

if __name__ == "__main__":
    report_dir = './test_report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="Appium_android_testreport", description="本测试报告内容包含88共享app简单测试")
        runner.run(discover)
