# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Selenium practice one
Step1:
Search for some result on google and print out that result.
Step2:
Click next and print the next page until page 10
Step3:
Close chrome
"""

# 创建一个 Chrome Webdriver 实例
driver = webdriver.Chrome(executable_path='../WebDrivers/chromedriver')

# 打开网址
driver.get('https://www.google.com/')

# 获取google输入框
search_input = driver.find_element_by_name("q")

# 输入内容
search_input.send_keys("python")

# Press Enter
search_input.submit()

"""
This part is important
这里的results_locator值是一个XPATH
而用chrome时，在需要元素上单击右键，点检查，会出现元素的代码
在元素的代码块上单击右键 -> Copy -> 单击 Copy XPATH
就会把所需要元素的XPATH复制到剪贴板，然后在python脚本里正常使用就可以了
---------------------------------------------------------
此处的click_next()中，就是利用XPATH选取了google.com上的Next按钮
然后直接click（） 进入下一页
---------------------------------------------------------
"""

def click_next():
    NEXT_BUTTON_LOCATOR = "//*[@id='pnnext']/span[2]"
    next_button = driver.find_element(By.XPATH, NEXT_BUTTON_LOCATOR)
    next_button.click()

def get_result():
    RESULTS_LOCATOR = "//div//h3"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, RESULTS_LOCATOR))
    )
    page_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)
    return page_results

def print_result(result):
    for item in result:
        print (item.text)

def print_all():
    page_result = get_result()
    print_result(page_result)
    click_next()

# Printing all results from 10 pages
for i in xrange(1,10):
    print_all()

# shut down the driver
driver.close()
