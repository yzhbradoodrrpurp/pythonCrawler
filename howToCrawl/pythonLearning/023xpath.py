# -*- coding = utf-8 -*-
# @Time: 2024/10/4 15:15
# @Author: Zhihang Yi
# @File: 023xpath.py
# @Software: PyCharm

from lxml import etree
"""
xpath可以解析本地的html文件，也可以解析服务器传过来的html文件。
xpath可以取代BeautifulSoup和re的作用。
"""

def main():
    # xpath解析本地文件用etree.parse(...)
    tree = etree.parse('local_file.html')
    # xpath解析服务器传来的文件用tree = etree.HTML(response.read().decode('utf-8'))，接下来的操作一样。

    """
    /查找直接的子节点，考虑层级关系；//查找子孙节点，不考虑层级关系。
    //li[@id]查找所有有id属性的li标签。
    //li[@id="..."]查找所有id为...的li标签。
    //li[@id="..." and @class="..."]可以查询所有id为...，class为...的li标签。
    //li[@id="..."]/@title可以得到id为...的li标签的title。
    //li[@id="..."]/text()可以得到id为...的li标签的文本。
    
    查询到的标签会组成一个列表然后返回。
    
    tag.text得到标签的文本内容。
    tag.get('...')得到...属性的内容。
    """
    cities = tree.xpath('//li')
    print(cities)

    for city in cities:
        print(city.text)


if __name__ == '__main__':
    main()
