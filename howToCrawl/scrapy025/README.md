# 一.注意事项：

## 1.关于start_urls:

    (1)如果start_urls是以html为后缀名的，那么一定要删除末尾的/。

    (2)如果不是以html为结尾的，那么删不删都可以。
        但是为了统一，一般建议删除。

## 2.关于xpath：
    
    Scrapy框架下的xpath和lxml的xpath使用方法大体上一致，但是有一些细节上的差别。
    
    (1)lxml的xpath：tree.xpath('...')得到的是标签或者标签的具体内容组成的列表。

    (2)Scrapy的xpath：response.xpath('...')得到的是关于Selector对象的列表(后面会详细解释什么是Selector对象)，
        然后使用get()/getall()函数可以提取Selector对象的文本或者特定内容。

## 3.关于Selector对象：

    (1)其实Selector对象和lxml中直接得到的标签是类似的。

    (2)e.g.:
        import scrapy
    
        class MySpider(scrapy.Spider):
        name = "example"
        start_urls = ["http://example.com"]
    
        def parse(self, response):
            # 创建 Selector 对象（response 本身就是一个 Selector）
            selector = response.xpath('//h1')  # 选择所有 <h1> 标签
    
            # 提取文本
            for h1 in selector:
                title = h1.xpath('text()').get()  # 获取每个 <h1> 的文本内容
                print(title)

## 4.关于get()函数：

    (1)其实get()函数等价于[0]，
        response.xpath('.../@title')[0] == response.xpath('.../@title').get(default='')。
        get()函数的好处在于，如果没找到，则[0]会报错IndexOutOfRange，而get()函数会返回一个默认值。


 # 二.Scrapy Shell：

## 1.Scrapy Shell简介：

    scrapy shell 是 Scrapy 提供的一个交互式命令行工具，用于快速测试和调试爬虫。
    它允许用户在一个交互式环境中与 Scrapy 的响应对象进行交互，便于进行网页内容的抓取和解析。
    
## 2.主要功能：

### (1).交互式测试：

    可以加载网页，并直接使用 XPath 或 CSS 选择器来提取数据，而无需编写完整的爬虫。

### (2).查看响应：

    使用 scrapy shell 可以方便地查看 HTTP 响应的内容和状态，以便调试。

### (3).快速实验：

    可以快速尝试不同的选择器和解析逻辑，以验证数据提取的有效性。

### (4).访问 Scrapy 功能：

    在 shell 中，你可以直接使用 Scrapy 的各种功能，如请求、解析和提取数据。

## 3.使用方式：

    打开terminal，直接输入：‘scrapy shell ...’ (...是网址的域名)。