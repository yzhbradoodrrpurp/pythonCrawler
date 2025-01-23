import scrapy


class BaiduTranslationSpider(scrapy.Spider):
    name = "baidu_translation"
    allowed_domains = ["fanyi.baidu.com"]
    # post请求如果没有参数，那么这个请求就不会生效。
    start_urls = ["https://fanyi.baidu.com/sug"]

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'what'
        }

        yield scrapy.FormRequest(url=url, callback=self.parse, FormData=data)

    def parse(self, response):
        print(response.text)
