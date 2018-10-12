# -*- coding: utf-8 -*-
import json
import scrapy
from six.moves.urllib import parse
from taobao.items import TaobaoItem
from scrapy.conf import settings
# instead of import parse from urllib


class MytaobaoSpider(scrapy.Spider):
    name = 'mytaobao'
    allowed_domains = ['taobao.com']
    # start_urls = ['http://taobao.com/']
    base_url = 'https://s.taobao.com/search?q=%s&sort=sale-desc&s=%s'
    
    start_urls = [
        'https://s.taobao.com/search?q=%s&sort=sale-desc&s=%s'
    ]
    cookie = settings['COOKIE']

    # 发送给服务器的http header, 有的网站需要伪装浏览器头，有的不需要
    headers = {
        'Connection': 'keep - alive', # 保持连接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
    }

    # 对请求的返回进行处理的配置
    meta = {
        'dont_redirect': True,
        'handle_httpstatus_list': [301, 302] # 对哪些异常返回进行处理
    }

    def start_requests(self):
        # 常量放置在setting.py中
        key_words = self.settings['KEY_WORDS']
        # 分析页面可以得到关键字传入内容会进行转码，空格会替换为+
        key_words = parse.quote(key_words,' ').replace(' ','+')
        page_num = self.settings['PAGE_NUM']
        count_per_page = self.settings['COUNT_PER_PAGE']
        for i in range(page_num):
            url = self.base_url % (key_words, i*count_per_page)
            yield scrapy.Request(url, callback=self.parse, cookies=self.cookie,
                headers=self.headers, meta=self.meta)

    def parse(self, response):
        # 使用scrapy内置的正则获取需要的内容
        p = 'g_page_config = ({.*?});'
        g_page_config = response.selector.re(p)[0]
        g_page_config = json.loads(g_page_config)
        auctions = g_page_config['mods']['itemlist']['data']['auctions']

        for auction in auctions:
            item = TaobaoItem() # 实例化item
            item['price'] = auction['view_price']
            item['deals'] = auction['view_sales']
            item['title'] = auction['raw_title']
            item['shop'] = auction['nick']
            item['location'] = auction['item_loc']
            item['detail_url'] = auction['detail_url']

            yield item # 将item传给生成器

