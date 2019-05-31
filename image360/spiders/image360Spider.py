# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode
import scrapy
from image360.items import Image360Item


class image360Spider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    # 重写Spider中的start_requests方法：指定开始url
    def start_requests(self):
        base_url = 'http://image.so.com/zj?'
        param = {'ch': 'beauty', 'listtype': 'new', 'temp': '1'}
        # 可以根据需要爬取不同数量的图片，此处只爬取60张图片
        for page in range(2):
            param['sn'] = page * 30
            full_url = base_url + urlencode(param)
            print(full_url)
            yield scrapy.Request(url=full_url, method='GET', callback=self.parse,encoding='utf-8')

    def parse(self, response):
        # 获取到的内容是json数据
        # 用json.loads(）解析数据
        # 此处的response没有content
        model_dict = json.loads(response.text)
        print(model_dict)
        for elem in model_dict['list']:
            item = Image360Item()
            item['title'] = elem['group_title']
            item['tag'] = elem['tag']
            item['height'] = elem['cover_width']
            item['width'] = elem['cover_height']
            item['url'] = elem['qhimg_url']
            yield item
