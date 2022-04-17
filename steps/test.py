"""
@Time ： 2022/4/17 16:34
@Auth ： heyeping
@File ：test.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import time
from behave import *
from assertpy import assert_that

@given("访问百度首页")
def step_impl(context):
    context.driver.get('http://www.baidu.com')

@when("输入关键字{keyword}")
def step_impl(context, keyword):
    # 模仿用户输入关键字
    context.driver.find_element_by_xpath('//*[@id="kw"]').send_keys(keyword)
    # 模仿用户点击按钮
    context.driver.find_element_by_xpath('//*[@id="su"]').click()

@then("验证返回的搜索结果标题为{result}")
def step_impl(context, result):
    time.sleep(2)
    assert_that(context.driver.title).is_equal_to(str(result))