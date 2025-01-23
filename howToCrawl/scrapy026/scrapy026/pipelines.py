# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import urllib.request

class Scrapy026Pipeline:
    def open_spider(self, spider):
        self.f = open('books.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item_dict = ItemAdapter(item).asdict()
        self.f.write(json.dumps(item_dict, ensure_ascii=False) + '\n')

        return item

    def close_spider(self, spider):
        self.f.close()


# 多条管道的开启。
class DownloadImages:
    def process_item(self, item, spider):
        item_dict = ItemAdapter(item).asdict()
        url = 'http:' + item_dict['img']
        urllib.request.urlretrieve(url=url, filename='./images/' + item_dict['name'] + '.jpg')

        return item
