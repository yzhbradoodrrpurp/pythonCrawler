# -*- coding = utf-8 -*-
# @Time: 2024/10/3 15:42
# @Author: Zhihang Yi
# @File: 019postKFC.py
# @Software: PyCharm

import urllib.request
import urllib.parse

def main():
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '成都',
        'pid': '',
        'pageIndex': 1,
        'pageSize': 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 '
            'Safari/605.1.15',
        'Cookie':
            'VOLCALB=e034eaec841777a5c7a8284a44165b90|1727941232|1727941123; '
            'route-cell=ksa; ASP.NET_SessionId=g1vflwy5l3rdxfspmrqdv2i2'
    }

    req = urllib.request.Request(url=url, data=data, headers=headers)

    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')

    with open('kfc.json', 'w') as f:
        f.write(content)
        f.close()


if __name__ == '__main__':
    main()
