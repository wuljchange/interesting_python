from selenium import webdriver
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    # 加载浏览器
    browser = webdriver.Chrome()
    # 获取页面
    browser.get('https://www.baidu.com')
    print(browser.page_source)
    # 查找单个元素
    input_first = browser.find_element_by_id('q')
    input_second = browser.find_element_by_css_selector('#q')
    input_third = browser.find_element(By.ID, 'q')
    # 查找多个元素
    input_elements = browser.find_elements(By.ID, 'q')
    # 元素交互操作，搜索框查询
