# -*- coding = utf-8 -*-
# @Time: 2024/9/15 14:59
# @Author: Zhihang Yi
# @File: 008crawlIntoWebpage1.py
# @Software: PyCharm

"""
爬虫的几个步骤：
1.爬取网页 2.解析数据 3.保存数据。
"""
import urllib.request


def main():
    url = input("Enter the site you want to crawl: ")
    crawl_webpage(url)  # 这一步属于爬取网页。


def crawl_webpage(url):  # 在这个函数中对爬取的网页进行数据处理，并将数据储存到变量data中。
    """
    urlopen()是一个urllib.request模块提供的函数，用于打开和读取url，并返回一个响应对象(网页的内容、数据等等)。
    有时服务器会检测到你正在爬虫所以迟迟不愿意给你响应结果，这就叫做超时。
    这个时候需要用到timeout=... ，表示...秒过后就结束爬取，并且会返回一个error。
    响应对象可以用read()函数读取网页的内容。
    由于响应对象通常是字节串，所以需要用decode(...)以utf-8的方式解码为字符串，得到的结果就是网页的源代码。
    """
    try:
        response = urllib.request.urlopen(url, timeout=3)
    except Exception as errorInfo:
        print("There is an error occurred: '{}'.".format(errorInfo))
    else:
        print("The source code of '{}' is:\n{}".format(url, response.read().decode('utf-8')))  # 响应对象包括网页源代码。
        print("The status code is {}.\n".format(response.status))  # 响应对象包括状态码。200是正常码，418是被服务器发现是爬虫了，404是没找到等等。
        print("The headers are as follows:\n {}.".format(response.headers))  # 响应对象也包括头部，其作用是在客户端和服务器之间传递一些特定信息。
    finally:
        print("The execution is done.")


if __name__ == "__main__":
    main()
