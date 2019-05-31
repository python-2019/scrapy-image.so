import json
import random
from urllib.parse import urlencode

import scrapy


class Amac2Spider(scrapy.Spider):
    name = 'local'
    allowed_domains = ['localhost']
    # custome_setting可用于自定义每个spider的设置，而setting.py中的都是全局属性的，当你的
    # scrapy工程里有多个spider的时候这个custom_setting就显得很有用了
    headers = {
        "Authorization": "3WsxKA4DGAhi8KK557iw2N"
    }

    # 需要重写start_requests方法
    def start_requests(self):
        # 测试本地 ajax
        base_url = "http://localhost:21031/api/ulms/saleOrder/myAllFollow?"
        # 所有请求集合
        for page in range(1, 3):
            random_random = random.random()
            # 封装post请求体参数
            my_data = {"page": page, "pageSize": 2}
            print("请求数据: " + str(my_data))
            # 模拟ajax发送post请求
            url = base_url + urlencode(my_data)
            print("请求完整url: " + url)
            yield scrapy.Request(url=url, method='GET',
                                 callback=self.parse_model,
                                 headers=self.headers,
                                 encoding='utf-8')

    def parse_model(self, response):
        # 可以利用json库解析返回来得数据，在此省略
        jsonBody = json.loads(response.body)
        # 拿到数据，再处理就简单了。不再赘述
        for row in jsonBody['data']['rows']:
            # 只打印 不返回管道处理
            print(str(row) + "\n")
            # yield jsonBody
