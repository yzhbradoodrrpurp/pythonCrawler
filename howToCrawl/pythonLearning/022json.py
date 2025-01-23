# -*- coding = utf-8 -*-
# @Time: 2024/10/4 12:46
# @Author: Zhihang Yi
# @File: 022json.py
# @Software: PyCharm

import urllib.request
import json
import jsonpath
"""
爬虫通常分为两大种方式：
第一种方式是去静态的html网页文件中爬取想要的数据；
第二种方式是去找到想要的接口，即json数据等等。
"""

def main():
    url = ('https://dianying.taobao.com/cityAction.json'
           '?activityId&_ksTS=1728017572589_108'
           '&jsoncallback=jsonp109'
           '&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
           )

    # content = crawl_page(url)

    try:
        # 淘票票网站上得到的json数据实际不是json数据，而是jsonp数据。
        # 这是一种反爬虫手段，我们将jsonp转换成json，所以自定义了一个transform_json()函数。
        # content = transform_json(content)
        # store_json(content)
        parse_json()
    except Exception as e:
        print('There\'s been an error occurred:')
        print(e)


def crawl_page(url):
    # 淘票票网有一些强烈反爬虫手段，只给出UA, Cookie信息还是会遭到拦截。
    # 所以这次我们将所有重要的头部信息都封装好了。
    headers = {
        'User-Agent':
            ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 '
            'Safari/605.1.15',
        'Cookie':
            'isg=BJ6eJ2wkdDZQN6BSCxeewtHP7TLgX2LZa5v8n0gnBuHdaz5FsO6q6egNY_fnyFrx; '
            'xlly_s=1; _tb_token_=ebf97e375e5af; '
            'cookie2=132f81d91d0150228a31433738848342; '
            't=d468e276a0dafa3eed6567ed57416ee9; v=0',
        'X-Requested-With':
            'XMLHttpRequest',
        'Accept':
            'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Language':
            'zh-CN,zh-Hans;q=0.9',
        'bx-v':
            '2.5.20',
        'Connection':
            'keep - alive',
        'Host':
            'dianying.taobao.com',
        'Referer':
            'https://dianying.taobao.com/'
    }

    try:
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
    except Exception as e:
        print(f'There\'s been a error:\n{e}')
        return
    else:
        print('You\'ve successfully crawled into the page!')
        return response.read().decode('utf-8')


def transform_json(content):
    # split()函数接收一个变量，以这个变量为界，划分成几个单独的元素，组成一个列表。
    # 在本次的情况中，jsonp109(...); ...就是json数据。
    # 所以我们取第二个元素。
    content = content.split('(')[1]
    # 由于末尾还有一个);，所以我们再进行一次split()。
    content = content.split(')')[0]
    # 另外，json中只能认可双引号，不认可单引号，所以我们需要进行替换。
    content = content.replace('\'', '\"')

    return content


def store_json(content):
    # # 爬取网页的步骤都是一样的，在这一步才有区别。
    # # 将爬取的json内容通过json.loads()函数解析为json格式下的Python对象(字典，字符串)。
    # content = json.loads(content)

    # 我们并不需要上面的这一步，因为我们可以直接将content(json格式)写入文件中。
    # 之所以保留上面的注释是为了知识的完整性。
    # json.loads()会将json格式的字符串转换为一个列表或者字典，这样就可以通过相应的方式进行访问。

    # 将得到的json格式文件保存下来。
    with open('taopiaopiao.json', 'w', encoding='utf-8') as f:
        # 将json格式的数据写入名为taopiaopiao.json的文件中。
        f.write(content)
        # 用了with open() as f: 就不用手动关闭文件了。离开这个结构以后，文件会自动关闭。


def parse_json():
    with open('taopiaopiao.json', 'r', encoding='utf-8') as f:
        # json.load()直接从文件本身读取json数据并将它返回为一个类型为str的Python变量，命名为data。
        # data的类型为字典。
        data = json.load(f)

    """
    $表示根元素，$.(...)表示根元素下面的(...)元素，$.(...).(...)表示根元素下面的(...)元素下面的(...)元素。
    $.(...).(...)[*]表示根元素下面的(...)元素下面的所有(...)元素。
    $..(...)表示所有的(...)元素。
    """

    # jsonpath()函数接收两个数据，第一个数据是在哪查询(必须是Python对象)，第二个是要查询的元素(用json语句表示)，然后返回一个列表。
    region_name = jsonpath.jsonpath(data, '$..regionName')
    print(region_name)


if __name__ == '__main__':
    main()
