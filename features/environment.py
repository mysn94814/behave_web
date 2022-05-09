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

from base.driverInit import driverInit


def before_scenario(context, feature):
    context.drivers = driverInit(index=2)
    print(context.drivers.driver1)


def after_scenario(context, feature):
    context.drivers.quits()


