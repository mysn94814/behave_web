# Gherkin.feature
Feature: 百度

  Scenario: 场景1-搜索关键字

    Given 关键字behave自动化测试
    When 打开百度页面https://www.baidu.com
    And 输入关键字
    And 点击百度一下按钮
    Then 页面中应包含关键字behave