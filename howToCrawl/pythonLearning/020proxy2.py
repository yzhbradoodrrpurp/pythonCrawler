# -*- coding = utf-8 -*-
# @Time: 2024/10/3 17:04
# @Author: Zhihang Yi
# @File: 020proxy2.py
# @Software: PyCharm

import urllib.request
import urllib.parse

def main():
    url = 'https://www.baidu.com'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 '
            'Safari/605.1.15'
    }

    req = urllib.request.Request(url=url, headers=headers)

    proxies = {
        'http': '118.24.219.151:16817',
        # 'https': '....'
    }
    # ProxyHandler()括号里接收一个字典，字典的形式如上面的proxy。
    # 这样操作就可以改变IP地址。
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(req)


if __name__ == '__main__':
    main()
