# 一.关于多页面的跳转：
    
## 1.e.g.:

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

            # meta是一个字典类型的变量，可以在不同的请求之间进行变量传递。
            yield scrapy.Request(url=link, callback=self.parse_image, meta={'name': name})

    def parse_image(self, response):
        name = response.meta['name']
        img = response.xpath('//div[@class="bd2"]//img/@src').get(default='None')

        movie_info = Scrapy027Item(name=name, img=img)

        yield movie_info

## 2.解释：

    同样是发送了一个新的请求:
        yield scrapy.Request(url=link, callback=self.parse_image, meta={'name': name}) 

    和之前其实只有两个地方不同：
        (1)parse_image是我们自己定义的类，用于在新的页面爬取数据。
        (2)meta是一个字典，用于将变量从原来方法传递到新的方法。
        
    所以在新的请求里爬取到了数据，然后再和原来的数据相结合，通过yield Scrapy027Item(...)提交给items.py，
    再在pipelines.py里进行存储的操作，逻辑就理顺了。


# 二.日志信息：

## 1.日志级别：

    CRITICAL: 严重错误
    ERROR: 一般错误
    WARNING: 警告
    INFO: 一般信息
    DEBUG: 调试信息

## 2.指定日志的级别：

    在setting.py加入 "LOG_LEVEL = '...'" ...是日志级别，严重程度在...以下的不会打印出来。

## 3.日志文件：

    在setting.py加入LOG_FILE = 'log_name.log' log_name是自定义的。
    日志文件的作用是将日志生成一个.log文件而不是打印在terminal里，LOG_LEVEL的作用在LOG_FILE中依然生效。