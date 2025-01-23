import scrapy


class CarhomeSpider(scrapy.Spider):
    name = "carHome"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://car.autohome.com.cn/price/brand-36.html"]

    def parse(self, response):
        # Scrapy框架下的xpath和lxml的xpath细节上有不同。
        cars = response.xpath('//div[@class="list-cont"]')
        car_list = []

        for car in cars:
            img = car.xpath('.//img[@loading="lazy"]/@src').get(default='')
            name = car.xpath('.//div[@class="main-title"]/a[@class="font-bold"]/text()').get(default='')
            price = car.xpath('.//div[@class="main-lever"]//span[@class="font-arial"]/text()').get(default='')

            car_list.append([name, price, img])
            print([name, price, img])



