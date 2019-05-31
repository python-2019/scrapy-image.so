# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Image360Item(scrapy.Item):
    title = scrapy.Field()
    tag = scrapy.Field()
    height = scrapy.Field()
    width = scrapy.Field()
    url = scrapy.Field()
