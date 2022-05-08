"""
@Time ： 2022/4/17 16:53
@Auth ： heyeping
@File ：environment.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from selenium import webdriver
import time
import os
import shutil

def before_scenario(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    time.sleep(1)


def after_scenario(context, feature):
    context.driver.quit()

