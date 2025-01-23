# -*- coding = utf-8 -*-
# @Time: 2024/9/16 10:25
# @Author: Zhihang Yi
# @File: 008crawlIntoWebpage3.py
# @Software: PyCharm

"""
008crawlIntoWebpage2.py中我们已经可以成功访问豆瓣top250榜单了。
但是那个top250并不是都在同一页上面，我们访问的榜单其实也只是第一页而已。
现在我们再次对我们的爬虫程序进行升级，让它能够爬取多个网页。
"""
import urllib.request


def main():
    url = input("Enter the starting webpage url: ")  # https://movie.douban.com/top250
    pages = int(input("How many pages do you want to crawl: "))  # 访问10页就能够将豆瓣top250的电影全部访问下来。

    for page in range(pages):
        url = url + "?start=" + str(page*25) + "&filter="  # 访问豆瓣top250的网站，查看url是如何变化的。
        crawl_webpage(url)


def crawl_webpage(url):
    headers = {
        "User-Agent":
            " Mozilla/5.0 (Macintosh; "
            "Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
        "Cookie":
            "__utma=30149280.1754311733.1724514622.1726453925.1726537386.8; "
            "__utmb=30149280.0.10.1726537386; __utmc=30149280; "
            "__utmz=30149280.1724650853.2.2.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; "
            "__utma=223695111.269374864.1726373946.1726453937.1726537386.6; __utmb=223695111.0.10.1726537386; "
            "__utmc=223695111; "
            "__utmz=223695111.1726453937.5.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; "
            "_pk_id.100001.4cf6=2a2c3a022884bf14.1726373946.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; "
            "_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1726537386%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; "
            "_vwo_uuid_v2=D79D948829DF5E1E2641A8268D7D4CAEE|f98ac244c6a908eca7ed9e9da8137ba8; "
            "__yadk_uid=iBnI7KXuQ53CBti0To244EKpjvqJKgNO; "
            "ll=\"108310\"; viewed=\"3211779_3259440_1291809_1015452_1035362_1212080_1020959_1079440_2334288\"; "
            "bid=ig7GY2FFDHA"
    }  # 封装headers的信息，包括Cookie, User-Agent等等，可以在开发者模式下的网页里查看。

    req = urllib.request.Request(url=url, headers=headers)  # 封装一个请求对象，模拟真实浏览器访问服务器时的样子。

    try:
        response = urllib.request.urlopen(req, timeout=3)
    except Exception as errorInfo:
        print("There's been an error:\n{}".format(erroInfo))
    else:
        print("You've successfully crawled into the webpage!")
        print("The source code of \"{}\" is as follows:\n{}".format(url, response.read().decode('utf-8')))
    finally:
        print("The whole execution is done.")


if __name__ == "__main__":
    main()
