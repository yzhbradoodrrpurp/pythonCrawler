# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy026Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    author = scrapy.Field()
    img = scrapy.Field()
    price = scrapy.Field()
    detail = scrapy.Field()
