# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import six.moves.urllib as urllib

"""
Selenium practice 2

抓取淘宝上的商品信息

TODO: Make scrapped data readable.
    (write a decoder)
"""


# Basic set up
chrome = webdriver.Chrome(executable_path='../WebDrivers/chromedriver')
wait = WebDriverWait(chrome, 10)    # wait time 10 sec
KEYWORD = 'PS4'     # search keyword
file_to_save = open('./scrapped_data/data_from_taobao.txt', 'w+')

def index_page(page):
    """
    打开/抓取 商品索引页
    """
    print 'Now scraping page ', page, '...'
    try:
        url = 'https://s.taobao.com/search?q=' + urllib.parse.quote(KEYWORD)
        chrome.get(url)
        if page > 1:
            # Jump to next avaliable page
            # input: 到第___页
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input'))
            )
            # submit: 确定
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
            )
            input.clear()           # 清空input里的内容
            input.send_keys(str(page))   # 在input里输入page_number
            submit.click()          # 点击“确定”
        # 等待当前页面和 page 匹配
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'), str(page))
        )
        # 等待商品加载
        # 商品CSS         
        # mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(1)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item'))
        )
        get_products()
    except TimeoutException:
        # Timeout, 重新加载
        index_page(page)

from pyquery import PyQuery as pq
def get_products():
    """
    获取商品信息
    """
    html = chrome.page_source   # Get page source code
    document = pq(html)         # Use PyQuery as parser
    items = document(".m-itemlist .items .item").items()    # get items
    for item in items:
        # parse product info we need
        product = {
            'price': item.find('.price').text(),     # 价格
            'deal': item.find('.deal-cnt').text(),   # 成交量
            'title': item.find('.title').text(),     # 商品名
            'shop': item.find('.shop').text(),       # 店名
            'location': item.find('.location').text()   # 发货位置
        }
        print >> file_to_save, product

MAX_PAGE = 10
def main():
    """
    We'll only go through 10 pages
    """
    for i in range(1, MAX_PAGE+1):
        index_page(i)

    print "I'm done and quitting program..."
    chrome.close()

main()