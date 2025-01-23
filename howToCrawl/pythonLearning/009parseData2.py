# -*- coding = utf-8 -*-
# @Time: 2024/9/17 10:06
# @Author: Zhihang Yi
# @File: 009parseData2.py
# @Software: PyCharm
"""
这一章里，我们学习文档的搜索功能。
"""
import urllib.request
from bs4 import BeautifulSoup
import re
# request是urllib中的一个子模块，BeautifulSoup是bs4中的一个子模块。
# 这两种引入方式其实是一样的。


def main():
    url = "https://www.baidu.com"  # 这一次我们先用百度的一个网页举例说明。
    crawl_webpage(url)


def crawl_webpage(url):
    headers = {  # 在开发者模式下得到https://www.baidu.com的headers相关信息。
        "user-Agent":
            "User-Agent: Mozilla/5.0 (Macintosh; "
            "Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"
    }

    req = urllib.request.Request(url=url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
    except Exception as ErrorInfo:
        print("There's been an error occurred:\n{}".format(ErrorInfo))
    else:
        parse_data(response.read().decode("utf-8"))


def parse_data(html):
    # 向BeautifulSoup()函数传入解析的对象(html)和解析器(html.parser，即解析类型)，会返回一个BeautifulSoup对象，这个对象就是树形结构。
    bs = BeautifulSoup(html, "html.parser")

    # find_all("...")函数会找到一个BeautifulSoup对象的所有名为...的标签，组成一个列表并返回。
    tags_named_a = bs.find_all(name="a")  # 当查询的内容只有名字时，可以省略name=。
    print(tags_named_a[0], tags_named_a[1], tags_named_a[2], sep='\n')

    # find_all("...")函数不仅可以查找标签名，也可以查找标签的属性，标签的文本内容等等。
    class_is_true = bs.find_all(class_=True)
    print(class_is_true[0], sep='\n')

    find_certain_str = bs.find_all(string="百度一下，你就知道")
    for find_str in find_certain_str:  # 输出的是string字符。
        print(find_str)

    find_several_strs = bs.find_all(string=["百度一下，你就知道", "微软雅黑"])  # 可以传入一个列表来查找多个字符串内容。
    for find_several_str in find_several_strs:
        print(find_several_str)  # 输出的同样只是字符，而不是整个标签。

    # find_all()函数还可以用limit限定搜索的个数。
    tags_named_a = bs.find_all(name="a", limit=3)  # 这样就限定了tags_named_a中只有3个名为a的标签。
    for tag_named_a in tags_named_a:
        print(tag_named_a)


if __name__ == "__main__":
    main()
