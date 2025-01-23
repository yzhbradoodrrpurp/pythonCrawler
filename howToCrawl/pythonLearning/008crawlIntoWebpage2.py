# -*- coding = utf-8 -*-
# @Time: 2024/9/15 17:08
# @Author: Zhihang Yi
# @File: 008crawlIntoWebpage2.py
# @Software: PyCharm

"""
008veryFirstCrawler1.py已经可以访问一些网站了，
不过这个代码段非常的初级，经常会遭到一些反爬虫手段的拦截。
用urlopen()直接打开一个url时，会带有一些特定的信息，服务器看到这些信息会触发反爬虫机制。
下面，我们对其进行一些升级，用Request()封装一个请求对象，用这个对象发起urlopen()申请。
这样一来，我们就可以模拟真实浏览器访问服务器时的场景，绕过反爬虫机制。
"""
import urllib.request


def main():
    url = "https://movie.douban.com/top250"
    crawl_webpage(url)


def crawl_webpage(url):

    headers = {  # 头部的内容可以在网站里查询，我们将头部的信息封装好，以伪造成真实浏览器访问时的样子，这样可以规避部分服务器反爬虫拦截。
        "method": "get",
        "scheme": "https",
        "User-Agent":
            "Mozilla/5.0 (Macintosh; "
            "Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
        "Cookie":
            "__utma=30149280.1754311733.1724514622.1726373940.1726384377.4; "
            "__utmc=30149280; "
            "__utmz=30149280.1724650853.2.2.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; "
            "__utma=223695111.269374864.1726373946.1726373946.1726384382.2; "
            "__utmc=223695111; "
            "__utmz=223695111.1726384382.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; "
            "_pk_id.100001.4cf6=2a2c3a022884bf14.1726373946.; "
            "_vwo_uuid_v2=D79D948829DF5E1E2641A8268D7D4CAEE|f98ac244c6a908eca7ed9e9da8137ba8; "
            "_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1726384382%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; "
            "__yadk_uid=iBnI7KXuQ53CBti0To244EKpjvqJKgNO; "
            "ll=\"108310\"; viewed=\"3211779_3259440_1291809_1015452_1035362_1212080_1020959_1079440_2334288\"; "
            "bid=ig7GY2FFDHA"  # Cookie太长了，我们可以分多行，Python会自动识别为一行。注意不能用'''，因为会包含换行符。
    }

    req = urllib.request.Request(url=url, headers=headers)  # 将url和封装好的headers交给Request()封装，创建一个请求对象。

    try:
        response = urllib.request.urlopen(req, timeout=3)  # urlopen()接收这个请求对象并发起一个请求，返回一个响应对象。
    except Exception as errorInfo:
        print("There's been an error: '{}'.".format(errorInfo))
    else:
        print("You've successfully crawled into the webpage!")
        print("The source code of {} is as follows:\n {}".format(url, response.read().decode('utf-8')))
    finally:
        print("The execution is done.")


if __name__ == "__main__":
    main()
