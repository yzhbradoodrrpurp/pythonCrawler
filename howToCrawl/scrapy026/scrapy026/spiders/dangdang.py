import scrapy
# 引入items.py文件下的一个类。
from scrapy026.items import Scrapy026Item


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.03.56.00.00.00.html"]

    # http://category.dangdang.com/cp01.03.56.00.00.00.html
    # http://category.dangdang.com/pg2-cp01.03.56.00.00.00.html
    # http://category.dangdang.com/pg3-cp01.03.56.00.00.00.html
    # http://category.dangdang.com/pg4-cp01.03.56.00.00.00.html
    pre_url = 'http://category.dangdang.com/pg'
    post_url = '-cp01.03.56.00.00.00.html'
    page = 1

    max_page = 10

    def parse(self, response):
        # pipelines: 用于下载数据。
        # items: 用于定义数据结构，通俗地说就是要下载的数据有什么。
        books = response.xpath('//div[@dd_name="普通商品区域"]//li')

        for book in books:
            name = book.xpath('./a/@title').get(default='None')
            author = book.xpath('.//p[@class="search_book_author"]//a[@name="itemlist-author"]/text()').get(default='None')
            price = book.xpath('.//p[@class="price"]/span[@class="search_now_price"]/text()').get(default='None')
            detail = book.xpath('.//p[@class="detail"]/text()').get(default='None')
            img = book.xpath('.//img/@data-original').get(default='None')

            # 防止图片的懒加载。
            if img == 'None':
                img = book.xpath('.//img/@src').get(default='None')

            # 将得到的数据传入items.py文件。
            book_info = Scrapy026Item(name=name, author=author, detail=detail, price=price, img=img)

            # yield类似于return，将book_info交给pipelines。
            # 注意：如果要使用pipeplines，就必须在settings中开启pipelines设置，解开注释。
            # 在settings.py中的pipelines相关那一行的数字是优先级，数字越小，优先级越高，范围在1～1000。
            yield book_info

        if self.page <= self.max_page:
            self.page += 1
            url = self.pre_url + str(self.page) + self.post_url

            yield scrapy.Request(url=url, callback=self.parse)
