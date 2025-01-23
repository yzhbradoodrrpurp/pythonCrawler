import scrapy
from scrapy027.items import Scrapy027Item

class MoviesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["www.dytt89.com"]
    start_urls = ["http://www.dytt89.com/html/tv/oumeitv/index.html"]

    def parse(self, response):
        movies = response.xpath('//div[@class="co_area2"]//ul//table[@class="tbspan"]')

        for movie in movies:
            name = movie.xpath('.//tr//td//b/a/text()').get(default='None')
            link = movie.xpath('.//tr//td//b/a/@href').get(default='None')
            link = 'http://www.dytt89.com' + link
            meta = {
                'name': name
            }

            # meta是一个字典类型的变量，可以在不同的请求之间进行变量传递。
            yield scrapy.Request(url=link, callback=self.parse_image, meta=meta)

    def parse_image(self, response):
        name = response.meta['name']
        img = response.xpath('//div[@class="bd2"]//img/@src').get(default='None')

        movie_info = Scrapy027Item(name=name, img=img)

        yield movie_info
