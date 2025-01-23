# -*- coding = utf-8 -*-
# @Time: 2024/9/17 19:38
# @Author: Zhihang Yi
# @File: 011crawl_parse.py
# @Software: PyCharm

# 用于爬取网页。
import urllib.request
# 用于解析网页数据。
from bs4 import BeautifulSoup
# 用于创建和分析正则表达式。
import re


def main():
    basic_url = input("Enter the webpage url that you want to crawl: ")  # https://movie.douban.com/top250
    pages = int(input("How many pages do you want to crawl: "))
    data_list = []

    for page in range(pages):
        url = basic_url + "?start=" + str(page*25) + "&filter="
        data_list.extend(crawl_page(url))

    for data in data_list:
        print(data)

def crawl_page(url):
    headers = {
        "Cookie":
            "__utma=30149280.1754311733.1724514622.1726453925.1726537386.8; "
            "__utmb=30149280.0.10.1726537386; __utmc=30149280; "
            "__utmz=30149280.1724650853.2.2.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; "
            "__utma=223695111.269374864.1726373946.1726453937.1726537386.6; __utmb=223695111.0.10.1726537386; "
            "__utmc=223695111; "
            "__utmz=223695111.1726453937.5.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; "
            "_pk_id.100001.4cf6=2a2c3a022884bf14.1726373946.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; "
            "_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1726537386%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; "
            "_vwo_uuid_v2=D79D948829DF5E1E2641A8268D7D4CAEE|f98ac244c6a908eca7ed9e9da8137ba8; "
            "__yadk_uid=iBnI7KXuQ53CBti0To244EKpjvqJKgNO; "
            "ll=\"108310\"; viewed=\"3211779_3259440_1291809_1015452_1035362_1212080_1020959_1079440_2334288\"; "
            "bid=ig7GY2FFDHA",
        "User-Agent":
            " Mozilla/5.0 (Macintosh; "
            "Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"
    }

    req = urllib.request.Request(url=url, headers=headers)

    try:
        response = urllib.request.urlopen(req, timeout=3)
    except Exception as errorInfo:
        print("There's been an error occurred:\n{}".format(errorInfo))
    else:
        return parse_data(response.read().decode("utf-8"))


def parse_data(html):
    # 将html文件解析后得到soup对象，是一个树形结构。
    soup = BeautifulSoup(html, "html.parser")

    # 找到soup树形对象中所有名为div，类别为item的标签(类型为Tag)，组成一个列表。
    films = soup.find_all(name="div", class_="item")

    # 用正则表达式创建一个用于形容链接表达式的标准模型，和标签a，超链接href组成查找对象。
    link_pattern = re.compile(r'<a href="(.*)">')
    # 末尾re.S的作用是让正则表达式.能够识别换行符。
    film_info_pattern = re.compile(r'<p class="">(.*?)</p>', re.S)
    quote_pattern = re.compile(r'<span class="inq">(.*)</span>')
    rating_num_pattern = re.compile(r'<span class="rating_num" property="v:average">(\d+\.\d+)</span>')
    rating_people_pattern = re.compile(r'<span>(\d+)人评价</span>')

    data_list = []

    for film in films:
        # 用find()函数在film标签内继续查找特定的标签。
        film_name = film.find(name="span", class_="title")

        # 注意film类型是标签，所以需要类型转换为字符串后才能用findall()查找特定的正则表达式，返回的是一个字符串组成的列表。我们只需要一个，所以加上[0]。
        # findall()函数查找的是完全匹配link_pattern的子字符串，并返回在这子字符串中的捕获组(.*)。
        link = link_pattern.findall(str(film))[0]
        rating_num = rating_num_pattern.findall(str(film))[0]
        rating_people = rating_people_pattern.findall(str(film))[0]

        # 对得到的信息进行一些格式上的处理。
        film_info = film_info_pattern.findall(str(film))[0]
        film_info = film_info.strip()
        film_info = film_info.replace("<br/>", "")
        film_info = film_info.replace(" "*28, "")
        film_info = film_info.replace("\xa0\xa0\xa0", "\n")
        film_info = film_info.replace("\xa0", " ")

        if len(quote_pattern.findall(str(film))) >= 1:
            quote = quote_pattern.findall(str(film))[0]

        # 其实查找某些特定的信息，用BeautifulSoup里的find()函数或者re里的findall()[0]都可以，看个人喜好，不过建议用findall()[0]正则表达式。

        if len(quote_pattern.findall(str(film))) >= 1:
            print("片名：{}\n{}\n简介：{}\n评分：{}\n评价人数：{}人\n链接：{}\n".format(film_name.string, film_info, quote, rating_num, rating_people, link))
            data_list.append([film_name.string, film_info, quote, rating_num, rating_people, link])
        else:
            print("片名：{}\n{}\n评分：{}\n评价人数：{}人\n链接：{}\n".format(film_name.string, film_info, rating_num, rating_people, link))
            data_list.append([film_name.string, film_info, "None", rating_num, rating_people, link])

    return data_list


if __name__ == "__main__":
    main()
