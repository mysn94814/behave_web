# Gherkin.feature
Feature: 测试Behave是否正常工作

  Scenario: 访问百度并搜索关键字
    Given 访问百度首页
    When 输入关键字jjj土豆
    Then 验证返回的搜索结果标题为土豆_百度搜索