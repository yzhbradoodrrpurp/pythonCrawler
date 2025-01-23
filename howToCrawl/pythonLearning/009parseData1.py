# -*- coding = utf-8 -*-
# @Time: 2024/9/17 10:42
# @Author: Zhihang Yi
# @File: 009parseData1.py
# @Software: PyCharm
"""
在爬取各个网页之后，我们得到的html数据还是不够直观。
这个时候我们需要对html数据进行解析，需要import beautifulsoup4。
beautifulsoup4的作用是将html文件转化为一个便于遍历的树形结构，
帮助开发者快速、方便地从网页中提取所需数据。
"""
import urllib.request
from bs4 import BeautifulSoup
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

    # title, a都是标签名，类型是Tag，会输出标签和标签里的内容(找到同名的第一个标签)。
    print("The type of \"{}\" is \"{}\".".format(bs.title, type(bs.title)))
    print("The type of \"{}\" is {}.".format(bs.a, type(bs.a)))

    # title, a依然是标签名，加上.string后类型是NavigableString，会输出标签里的内容而不输出标签。
    print("The type of \"{}\" is {}.".format(bs.title.string, type(bs.title.string)))
    print("The type of \"{}\" is {}.".format(bs.a.string, type(bs.a.string)))

    # title, a依然是标签名，加上.attrs后类型是dict，字典里面包含了这个标签的属性。
    print("The type of \"{}\" is {}.".format(bs.a.attrs, type(bs.a.attrs)))
    print("The type of \"{}\" is {}.".format(bs.title.attrs, type(bs.title.attrs)))

    # 如果bs后面不加任何标签，类型为BeautifulSoup，表示整个文档。
    print("The type of \"{}\" is {}.".format(bs, type(bs)))

    """
    用BeautifulSoup()函数解析过后的文档包含四种类型的变量，分别为Tag, NavigableString, BeautifulSoup, Comment。
    以上已经提及了前面三种类型，Comment类型就是html的注释。
    用.string不会显示出标签的注释内容，但是用type(...)会显示出标签的注释类型。
    """


if __name__ == "__main__":
    main()
