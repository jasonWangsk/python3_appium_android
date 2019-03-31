#!usr/bin/env python3
# -*-coding:utf-8-*-
# todo:元素读取
import os
from configparser import ConfigParser

def elements_read():

    file_path = str(os.path.dirname(os.path.dirname(__file__)))
    file_path = file_path.replace('\\', '/')
    cfg_path = file_path + '/config/config.cfg'
    config = ConfigParser()
    config.read(cfg_path, encoding='utf-8')
    return config

elements_read()

