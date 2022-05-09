"""
@Time ： 2022/5/8 12:51
@Auth ： heyeping
@File ：baidu_page.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from selenium.webdriver.common.by import By
from base.base import Base


class BaiduPage(Base):
    elem_input_wd = (By.NAME, "wd")  # 百度首页输入框
    elem_click_su = (By.ID, "su")  # 百度一下按钮

    # 以下为类的初始化函数，其又调用了父类的初始化函数，这样做的目的是为了
    # 将context.driver串起来，在调用PO类时，可以使用超级全局变量context下的driver对象
    def __init__(self, driver):
        super(BaiduPage, self).__init__(driver)

    def input_wd(self, words):
        self.base_input(self.elem_input_wd, words)

    def click_su(self):
        self.base_click(self.elem_click_su)

    # 判读link_text中是否包含关键词本文
    def exist_word(self, word):
        self.base_link_text_is_exist(word)

