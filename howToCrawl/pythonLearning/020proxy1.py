# -*- coding = utf-8 -*-
# @Time: 2024/10/3 16:23
# @Author: Zhihang Yi
# @File: 020proxy1.py
# @Software: PyCharm
"""
有时候需要使用别的IP地址来访问网站，
那么就需要使用到IP代理技术。
这个时候先介绍handler处理器。
"""
import urllib.request
import urllib.parse
import json


def main():
    url = 'https://www.baidu.com'

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 '
            'Safari/605.1.15'
    }

    req = urllib.request.Request(url=url, headers=headers)

    # HTTPHandler是一个处理HTTP请求的类，创建了这个类并赋值给handler。
    handler = urllib.request.HTTPHandler
    # build_opener()接收一个处理对象并创建一个打开器。
    opener = urllib.request.build_opener(handler)
    # 这个打开器可以处理url请求，管理请求的发送，处理 HTTP 响应，以及实现其他功能，如使用代理等。
    response = opener.open(req)
    content = response.read().decode('utf-8')
    print(content)

    # 以上的代码和之前的一样，满足一个简单的爬取网页源代码的功能。
    # 进阶的IP代理功能放在下一章介绍。


if __name__ == '__main__':
    main()
