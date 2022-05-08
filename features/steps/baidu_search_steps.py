"""
@Time ： 2022/5/8 12:52
@Auth ： heyeping
@File ：baidu_search_steps.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# @effect：百度搜索的BDD步骤实现场景
import time
from behave import *
from page.baidu_page import BaiduPage


@given("关键词{words}")
def step_impl(context, words):  # context是上下文对象，有参数的话，加上对应参数
    context.words = words  # 将参数绑定上下文对象，以便其他步骤使用


@when("打开百度页面{url}")
def step_impl(context, url):
    BaiduPage(context).get_url(url)
    time.sleep(1)


@when("输入关键词")
def step_impl(context):
    BaiduPage(context).input_wd(context.words)
    time.sleep(0.5)


@when("点击百度一下按钮")
def step_impl(context):
    BaiduPage(context).click_su()
    time.sleep(0.5)


@then("页面中应包含关键词{keyword}")
def step_impl(context, keyword):
    BaiduPage(context).exist_word(keyword)
    time.sleep(2)