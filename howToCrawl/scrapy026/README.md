# 一.Scrapy框架下每个文件的功能：

## 1.items：
    
### (1)简介：

    用于定义数据结构，通俗的来说就是需要下载的内容有哪些。

### (2)e.g.:

    import scrapy
         
    class Scrapy026Item(scrapy.Item):

        name = scrapy.Field()
        author = scrapy.Field()
        img = scrapy.Field()
        price = scrapy.Field()
        detail = scrapy.Field()

### (3)数据传送：
    
    将主爬虫程序爬取下来的数据name, author, detail, price, img通过Scrapy026Item()传送给items.py文件。
    注意要在主爬虫程序的开头加上'from scrapy026.items import Scrapy026Item'，从这个文件中引入这个类。

    book_info = Scrapy026Item(name=name, author=author, detail=detail, price=price, img=img)

    注意：
        在 Scrapy 中，item 通常是一个类的实例，而不是标准的字典。
        虽然 Scrapy 的 item 类实现了字典的行为（比如可以用类似字典的方式访问数据），但它不是纯粹的字典。

## 2.pipelines：

### (1)简介：

    pipelines.py 文件在 Scrapy 框架中用于处理爬取到的数据。
    你可以在这里定义数据处理管道，例如清洗数据、验证数据、存储数据到数据库或文件等。
    每个管道都可以独立处理数据，使得数据处理流程更加灵活和可维护。

### (2)注意事项:
    
    在主爬虫程序得到的数据必须通过yield传送给pipelines.py。

    使用pipelines.py首先要在settings.py中将关于pipelines.py的注释解开。
    注释中的那一行有个数值，范围是1～1000，代表优先级。数值越小，优先级越高。

    主程序将爬取的结果yield给pipelines.py，pipelines.py中的item变量接收了这个结果。

### (3)pipelines中的函数：

    e.g.:
        class Scrapy026Pipeline:
        def open_spider(self, spider):
            self.f = open('books.json', 'w', encoding='utf-8')
    
        def process_item(self, item, spider):
            f.write(json.dumps(item))
    
            return item
    
        def close_spider(self, spider):
            self.f.close()

    open_spider(), process_item(), close_spider()都是Scrapy框架下，pipelines中固定的方法。
    open_spider()只会在爬虫开始时运行一次，用于初始化操作，比如打开文件或数据库连接。
    close_spider() 在爬虫结束时调用，用于清理资源，比如关闭文件或数据库连接。
    process_item()则会在整个爬虫周期中重复运行。
    这样的架构方式确保了文件的打开或关闭在整个爬虫过程中只运行一次，提高了效率。

### (4)关于yield：
    
    yield 是 Python 中的一种关键字，用于定义生成器（generator）。
    当你在一个函数中使用 yield 时，这个函数就变成了一个生成器，能够一次返回一个值，
    并在下次调用时继续从上次返回的位置继续执行。

    生成器在 yield 语句处暂停执行，保留当前状态，下一次调用时可以继续从那里恢复。

    与return的区别：
        yield 会保存函数的当前状态，并在下一次调用时从该状态继续执行。
        而 return 则会终止函数的执行，并返回一个值，函数的状态不会被保存，之后再调用该函数时会从头开始执行。
        这个特性使得生成器非常适合处理大量数据或需要懒加载的场景。

    e.g.:
        def count_up_to(max):
            count = 1
            while count <= max:
                yield count
                count += 1
    
        counter = count_up_to(5)
        for number in counter:
        print(number)

### (5)关于ItemAdapter(...).asdict()和json.dumps()：
    
    ItemAdapter() 是 Scrapy 提供的一个类，用于在 Scrapy 的 item 和标准 Python 数据结构之间进行转换。
    
    asdict() 是 ItemAdapter 提供的方法，用于将 Scrapy item（通常是类的实例）转换为标准的 Python 字典。
    这个方法会遍历 item 的所有字段，并返回一个包含这些字段及其值的字典。

    json.dumps()接收一个Python对象(一般是字典类型),然后将其转换为json字符串。
    这种方式相对于str()的好处是可以确保格式的正确。
    json.dumps()和json.loads()是相反功能的函数。

    ensure_ascii 是 json.dumps() 函数的一个参数，用于控制非 ASCII 字符的处理方式。
    当 ensure_ascii=True（默认值）时，所有非 ASCII 字符都会被转义为 Unicode 码点，例如中文字符会变成 \u4e2d\u6587。
    当 ensure_ascii=False 时，非 ASCII 字符将以原始形式输出，这样可以保留字符的可读性，例如中文字符会直接显示为“中文”。

### (6)多管道的开启：

    e.g.:
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

    在pipelines.py自定义一个类，然后加上process_item()函数(必要的话加上open_spider()/close_spider())。

    然后在settings.py中的ITEM_PIPELINES字典中加上类名和数值。


# 二.图片的懒加载：

## 1.说明：

    当一个网页中有大量图片时，为了防止加载缓慢，会对图片实施懒加载。
    通俗地说，在屏幕之外的图片的url名和在屏幕之内url名不同。
    在爬取图片的时候需要注意这一点。

## 2.e.g.:

    for book in books:
        img = book.xpath('.//img/@src').get(default='None')

        # 防止图片的懒加载。
        if img == 'None':
            img = book.xpath('.//img/@data-original').get(default='None')

        print(img)


# 三.多页爬取：

## 1.e.g.:

    class DangdangSpider(scrapy.Spider):
        name = "dangdang"
        allowed_domains = ["category.dangdang.com"]
        start_urls = ["http://category.dangdang.com/cp01.03.56.00.00.00.html"]

        pre_url = 'http://category.dangdang.com/pg'
        post_url = '-cp01.03.56.00.00.00.html'
        page = 1
        

        def parse(self, response):
            ...(每一页具体的爬虫程序)
            ...(每一页具体的爬虫程序)
            ...(每一页具体的爬虫程序)
    
            if self.page < 100:
                self.page += 1
                url = self.pre_url + str(self.page) + self.post_url
        
                yield scrapy.Request(url=url, callback=self.parse)

## 2.解释：

### (1)关于scrapy.Request():

    scrapy.Request() 是 Scrapy 框架中的一个类，用于创建一个新的 HTTP 请求对象。
    这个请求对象包含了要访问的 URL 以及其他一些可选参数。

### (2)关于callback=self.parse:
    
    callback 是 scrapy.Request 的一个参数，用于指定当请求完成时要调用的函数。
    这意味着当 Scrapy 接收到响应后，它会自动将响应传递给你指定的回调函数进行处理。
    
    当你在 scrapy.Request 中使用 callback=self.parse 时，Scrapy 会在请求完成后自动调用 self.parse 方法。
    如果不指定 callback，则响应将不会被处理，Scrapy 将不会知道该如何处理返回的数据。
    
    parse就是主爬虫程序的方法名，注意不能加括号。

### (3)关于yield：

    虽然 parse 函数看起来并不直接返回内容，但它实际上通过 yield 返回并执行了新的请求。
    如果你只是写了 scrapy.Request(...) 而不使用 yield，Scrapy 会创建一个请求对象，但这个请求不会被调度执行。
    这是因为在 Scrapy 的工作流中，只有通过 yield 或 return 将生成的请求返回，Scrapy 才能知道需要去执行这个请求。

    在 Scrapy 中，如果你希望 parse 函数能够发起新的请求(即多页爬取)，那么使用 yield 是必需的。
    
    注意：不能将yield改为return，因为这不会将新的请求加入调度队列。


    