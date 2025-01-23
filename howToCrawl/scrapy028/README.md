# 一.Scrappy框架下的POST请求：

## 1.post请求必须接收一个参数：

    原因在于post请求必须接收一个参数，否则post请求不生效。
    而当直接设定start_urls为post请求的url时，并没有传递参数。

    e.g.:
        def start_requests(self):
            url = 'https://fanyi.baidu.com/sug'
    
            data = {
                'kw': 'what'
            }
    
            yield scrapy.FormRequest(url=url, callback=self.parse, FormData=data)
    
        def parse(self, response):
            print(response.text)

## 2.关于start_requests():
    
    start_requests()是Scrapy框架下Spider类的一个内置方法。
    当需要使用post请求\添加头部信息时，就需要重写start_requests()函数。

## 3.关于scrapy.FormRequest()：
    
    scrapy.Request()发一个get请求，scrapy.FormRequests()发起一个post请求。
    其中Formdata变量接收一个字典，字典里就是需要查询的内容。