"""
@Time ： 2022/4/17 16:26
@Auth ： heyeping
@File ：seleApi.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

from selenium import webdriver
class SeleApi:
    def step_startup(self):
        self.driver = webdriver.chrome()
        self.driver.get("https://www.baidu.com/")

    def step_click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def step_send_keys(self, xpath, xpath_value):
        self.driver.find_element_by_xpath(xpath).send_keys(xpath_value)

    def step_text(self, cssselector):
        ele_results = self.driver.find_element_by_css_selector(cssselector).text
        return ele_results

    def step_quit(self):
        self.driver.quit()








