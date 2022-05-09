#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : driverInit.py
# @Author: maoyushaonian 
# @Date  : 2022/5/9
# @Desc  :
from selenium import webdriver
import time

class driverInit:
    def __init__(self, index=1):
        self.index=index
        names = self.__dict__
        for i in range(index):
            driver = names['driver' + str(i + 1)] = webdriver.Chrome()
            driver.implicitly_wait(10)
            driver.maximize_window()


    def quits(self):
        for i in range(self.index):
            self.__getattribute__('driver{0}'.format(str(i+1))).quit()

