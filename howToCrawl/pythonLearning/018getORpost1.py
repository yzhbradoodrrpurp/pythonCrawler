# -*- coding = utf-8 -*-
# @Time: 2024/10/3 14:15
# @Author: Zhihang Yi
# @File: 018getORpost1.py
# @Software: PyCharm
"""
post请求方式相比于request请求方式更加的安全。
"""

import urllib.request
import urllib.parse
import json


def main():
    url = 'https://fanyi.baidu.com/sug'

    # 在post请求方式下，请求内容必须放在data里，再通过Request()封装成一个请求对象。
    # 在get请求方式下，请求内容就在url里。
    data = {
        'kw': 'spider'
    }
    # urlencode()函数接收一个字典，将字典的值转换为unicode并将不同的键值对通过&连接起来形成一个字符串。
    # encode()函数接收一个字符串和这个字符串原本的解码类型，然后将这个字符串编码为字节。
    # 编码的原因在于：在之后封装一个请求对象时，data的类型必须是字节型。
    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) '
            'Version/18.0 Safari/605.1.15'
    }

    # 将url, 请求内容, 头部信息封装成一个请求对象，注意data的类型必须是字节型。
    req = urllib.request.Request(url=url, data=data, headers=headers)
    response = urllib.request.urlopen(req)
    # 返回的响应内容是一个json类型的数据可以对其进行json解码。
    content = response.read().decode('utf-8')
    print(content)
    json_content = json.loads(content)
    print(json_content)


if __name__ == '__main__':
    main()