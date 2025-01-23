import scrapy


class BaiduSpiderSpider(scrapy.Spider):
    # 爬虫的名字，用于运行爬虫时使用的值。
    name = "baidu_spider"
    # 允许访问的域名，只能访问这个域名及其子域名。
    allowed_domains = ["www.baidu.com"]
    # 起始访问url地址，就是第一次需要访问的地址，然后通过这个地址去到其它地址。
    start_urls = ["https://www.baidu.com"]

    # 这个方法是执行了start_urls之后执行的方法，response就是response = urllib.request.urlopen(...)得到的那个response。
    def parse(self, response):
        print("Hello World!")
