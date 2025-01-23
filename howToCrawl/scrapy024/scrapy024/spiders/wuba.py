import scrapy


class WubaSpider(scrapy.Spider):
    name = "wuba"
    allowed_domains = ["cd.58.com"]
    start_urls = ["https://cd.58.com/quanzhizhaopin/?key=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88"]

    def parse(self, response):
        # 获取网页的html源码。
        print(response.text)
        # 获取二进制数据。
        print(response.body)
        # 可以直接使用xpath来得到路径和标签。
        salary_list = response.xpath('//ul[@id="list_con"]/li[@class="job_item"]//p[@class="job_salary"]')
        # 用extract()函数提取出标签。
        print(salary_list.extract())


