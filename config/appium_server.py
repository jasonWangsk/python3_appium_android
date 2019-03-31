
import os
import time
from common.log import LOG,logger

# TODO:封装启动/关闭appiumserver

# pc = input('请输入系统 win or mac：')
pc = ('mac')
@logger('appiumserver...')
def stop_appium(post_num=4723):
    '''关闭appium服务'''
    if pc.upper() =='WIN':   # UPPER:将字符串中的小写字母转为大写字母。
        p = os.popen(f'netstat  -aon|findstr {post_num}')
        p0 = p.read().strip()
        if p0 != '' and 'LISTENING' in p0:
            p1 = int(p0.split('LISTENING')[1].strip()[0:4])  # 获取进程号
            os.popen(f'taskkill /F /PID {p1}')  # 结束进程
            LOG.info('appium server已结束...')
            # print('\n','appium server已结束...')
    elif pc.upper() == 'MAC':
        p = os.popen(f'lsof -i tcp:{post_num}')
        p0 = p.read()
        if p0.strip() != '':
            p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
            os.popen(f'kill {p1}')  # 结束进程
            # print('\n','appium server已结束...')
            LOG.info('appium server已结束...')


def start_appium(post_num=4723):
    '''开启appium服务'''
    stop_appium(post_num)    # 先判断端口是否被占用，如果被占用则关闭该端口号
    # 根据系统，启动对应的服务
    cmd_dict = {
        'WIN':f' start /b appium -a 127.0.0.1 -p {post_num} --log appium_run_server.log --log-level error --local-timezone ',
        'MAC':f'appium -a 127.0.0.1 -p {post_num} --log /Users/tester/project/android_autotest-master/testlog/appium_run_server.log --log-level error  --local-timezone  & '
    }
    os.system(cmd_dict[pc.upper()])
    time.sleep(3)  # 等待启动完成
    LOG.info('appium server 启动成功...')

    # print('appium server 启动成功...','\n')

if __name__ == '__main__':
    stop_appium()
    start_appium()
