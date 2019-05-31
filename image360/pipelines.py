# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from image360.items import Image360Item


class Image360Pipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if isinstance(item, Image360Item):
            url = item['url']
            print(url)
            yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        # 将下载的图片路径（传入到results中）存储到 image_paths 项目组中，如果其中没有图片，我们将丢弃项目:
        image_path = [x['path'] for ok, x in results if ok]
        # # 上面的语句 可以写成
        # for ok, x in results:
        #     if ok:
        #         image_path = x['path']
        if not image_path:
            raise DropItem("Item contains no images")
        return item
