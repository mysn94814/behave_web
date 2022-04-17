"""
@Time ： 2022/4/17 16:53
@Auth ： heyeping
@File ：environment.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()

def after_scenario(context, scenario):
    context.driver.close()

