# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    deals = scrapy.Field()
    title = scrapy.Field()
    shop = scrapy.Field()
    location = scrapy.Field()
    detail_url = scrapy.Field()
    pass
