# -*- coding = utf-8 -*-
# @Time: 2024/10/3 14:51
# @Author: Zhihang Yi
# @File: 018getORpost2.py
# @Software: PyCharm

import urllib.request
import urllib.parse
import json


def main():
    url = 'https://fanyi.baidu.com/ait/text/translate'

    # 很多时候，post请求下的请求内容不止一个。
    data = {"query": "spider",
            "from": "en",
            "to": "zh",
            "reference": "",
            "corpusIds": [],
            "needPhonetic": true,
            "domain": "common",
            "milliTimestamp": 1727938562391
            }
    # urlencode()函数接收一个字典，将字典的值转换为unicode并将不同的键值对通过&连接起来形成一个字符串。
    # encode()函数接收一个字符串和这个字符串原本的解码类型，然后将这个字符串编码为字节。
    # 编码的原因在于：在之后封装一个请求对象时，data的类型必须是字节型。
    data = urllib.parse.urlencode(data).encode("utf-8")

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) '
            'Version/18.0 Safari/605.1.15'
    }

    req = urllib.request.Request(url=url, data=data, headers=headers)

    response = urllib.request.urlopen(req)
    content = response.read().decode("utf-8")
    print(content)
    json_content = json.loads(content)
    print(jspn_content)


if __name__ == '__main__':
    main()
