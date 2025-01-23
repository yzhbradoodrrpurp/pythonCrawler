# -*- coding = utf-8 -*-
# @Time: 2024/9/25 15:23
# @Author: Zhihang Yi
# @File: 016crawl_parse_storeBOTH.py
# @Software: PyCharm

# 作用是爬取网页。
import urllib.request
# 作用是将爬取下来的html文件转换成一个树形结构的BeautifulSoup对象，便于查取信息。
from bs4 import BeautifulSoup
# 作用是引入正则表达式，通过正则表达式查找想要的文本内容。
import re
# 作用是将得到的数据保存为.xls格式。
import xlwt
# 作用是将得到的数据保存为.db格式。
import sqlite3


def main():
    # https://movie.douban.com/top250
    # /Users/yzhbradoodrrpurp/Desktop/douban_films_top250.xls
    # /Users/yzhbradoodrrpurp/Desktop/douban_films_top250.db
    basic_url = input("Enter the starting webpage url that you want to crawl: ")
    pages = int(input("How many pages do you want to crawl: "))
    storage_location_xls = input("Enter the location to save the file.xls: ")
    storage_location_db = input("Enter the location to save the file.db: ")
    data_list = []

    for page in range(pages):
        # 通过特定的规律，得到多个网页的url，循环爬取多个网页。
        url = basic_url + "?start=" + str(page*25) + "&filter="

        data_each_page = crawl_page(url)
        data_list.extend(data_each_page)
        print("Page %d is successfully crawled, parsed and stored.\n" % (page + 1))

    # 将想要保存的地址和数据给到函数，函数会将数据保存到相应的地址里。
    # 地址的格式是：路径/文件名。
    store_data_xls(storage_location_xls, data_list)
    store_data_db(storage_location_db, data_list)

    print("All execution is done.")


def crawl_page(url):
    # 封装请求的头部内容，包括Cookie, User-Agent等，伪装成正常的浏览器访问。否则会被网页的反爬虫程序拦截。
    headers = {
        # Cookie, User-Agent可以在网页的开发者模式下查看。
        "Cookie":
            "pk_id.100001.4cf6=2a2c3a022884bf14.1726373946.; "
            "_pk_ses.100001.4cf6=1; "
            "__utma=30149280.1754311733.1724514622.1726755319.1726820717.13; "
            "__utmb=30149280.0.10.1726820717; __utmc=30149280; "
            "__utmz=30149280.1724650853.2.2.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; "
            "__utma=223695111.269374864.1726373946.1726755319.1726820717.11; __utmb=223695111.0.10.1726820717; "
            "__utmc=223695111; "
            "__utmz=223695111.1726453937.5.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; "
            "ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1726820717%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; "
            "_vwo_uuid_v2=D79D948829DF5E1E2641A8268D7D4CAEE|f98ac244c6a908eca7ed9e9da8137ba8; "
            "__yadk_uid=iBnI7KXuQ53CBti0To244EKpjvqJKgNO; "
            "ll=\"108310\"; viewed=\"3211779_3259440_1291809_1015452_1035362_1212080_1020959_1079440_2334288\"; bid=ig7GY2FFDHA",
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15"
               }

    # 将url, headers封装成一个请求对象，然后用这个请求对象去申请打开网页。
    req = urllib.request.Request(url=url, headers=headers)

    try:
        # 尝试打开网页，设置超时时间为3秒。若成功则返回一个响应对象。
        response = urllib.request.urlopen(req, timeout=3)
    except Exception as errorInfo:
        print("There's been an error occurred:\n{}".format(errorInfo))
        return ["Nothing on this page."]
    else:
        # 响应对象里包含了网页的html文件用如下方式得到。
        html = response.read().decode("utf-8")
        data_each_page = parse_data(html)

    return data_each_page


def parse_data(html):
    # 用BeautifulSoup()函数将得到的html文件通过html.parer的解码方式转换成一个树形的BeautifulSoup对象。
    soup = BeautifulSoup(html, "html.parser")
    # 可以用find_all()函数通过标签名和标签里的属性查找特定的标签(类型为标签)，并返回一个列表。
    films = soup.find_all(name="div", class_="item")
    data_each_page = []

    # 用正则表达式创立一个模版，便于后面通过模版得到想要的信息。
    film_name_pattern = re.compile(r'<span class="title">(.*?)</span>')
    original_name_pattern = re.compile(r'<span class="title">\xa0/\xa0(.*?)</span>')
    creators_pattern = re.compile(
        r'''<p class="">
                            (.*?)<br'''
    )
    film_details_pattern = re.compile(
        r'''
                            (.*?)
                        </p>'''
    )
    rating_num_pattern = re.compile(r'<span class="rating_num" property="v:average">(\d+\.\d+)</span>')
    rating_people_pattern = re.compile(r'<span>(.*?)</span>')
    quote_pattern = re.compile(r'<span class="inq">(.*?)</span>')
    link_pattern = re.compile(r'<a href="(.*?)">')
    image_pattern = re.compile(r'src="(.*?)" ')

    for film in films:
        # 通过findall(...)函数在...字符串(由于film是标签，需要类型转换)中查找匹配模版的信息，并将模版中括号里的内容返回，组成一个列表。
        film_name = film_name_pattern.findall(str(film))[0]
        creators = creators_pattern.findall(str(film))[0]
        film_details = film_details_pattern.findall(str(film))[0]
        rating_num = rating_num_pattern.findall(str(film))[0]
        rating_people = rating_people_pattern.findall(str(film))[0]
        link = link_pattern.findall(str(film))[0]
        image = image_pattern.findall(str(film))[0]

        if len(original_name_pattern.findall(str(film))) != 0:
            original_name = original_name_pattern.findall(str(film))[0]

        if len(quote_pattern.findall(str(film))) != 0:
            quote = quote_pattern.findall(str(film))[0]

        if len(original_name_pattern.findall(str(film))) != 0:
            if len(quote_pattern.findall(str(film))) != 0:
                print(
                    "名字：{}\n原名：{}\n{}\n类型：{}\n评分：{}\n评分人数：{}\n介绍：{}\n链接：{}\n图片：{}"
                    .format(film_name, original_name, creators, film_details, rating_num, rating_people, quote, link, image)
                )
                data_each_page.append([film_name, original_name, creators, film_details, rating_num, rating_people, quote, link, image])
            else:
                print(
                    "名字：{}\n原名：{}\n{}\n类型：{}\n评分：{}\n评分人数：{}\n链接：{}\n图片：{}"
                    .format(film_name, original_name, creators, film_details, rating_num, rating_people, link, image)
                )
                data_each_page.append([film_name, original_name, creators, film_details, rating_num, rating_people, "None", link, image])
        else:
            if len(quote_pattern.findall(str(film))) != 0:
                print(
                    "名字：{}\n{}\n类型：{}\n评分：{}\n评分人数：{}\n介绍：{}\n链接：{}\n图片：{}"
                    .format(film_name, creators, film_details, rating_num, rating_people, quote, link, image)
                )
                data_each_page.append([film_name, film_name, creators, film_details, rating_num, rating_people, quote, link, image])
            else:
                print(
                    "名字：{}\n{}\n类型：{}\n评分：{}\n评分人数：{}\n链接：{}\n图片：{}"
                    .format(film_name, creators, film_details, rating_num, rating_people, link, image)
                )
                data_each_page.append([film_name, film_name, creators, film_details, rating_num, rating_people, "None", link, image])
        print()

    return data_each_page


def store_data_xls(storage_location_xls, data_list):
    # 用Workbook(...)函数新建一个xls文件，...是解码方式，返回一个文件对象命名为workbook。
    workbook = xlwt.Workbook(encoding="utf-8")
    # 在workbook里新建一个名为douban_films_top250的表单页，返回一个表单页对象命名为worksheet1。
    worksheet1 = workbook.add_sheet("douban_films_top250")

    headlines = ("中文名", "原名", "主创人员", "类型", "评分", "评分人数", "介绍", "链接", "封面")

    for headline in range(len(headlines)):
        # 用write()函数在表单页中填写内容。第一个变量表示行，第二个变量表示列，第三个变量表示内容。
        worksheet1.write(0, headline, headlines[headline])

    for i in range(0, len(data_list)):
        for j in range(len(data_list[i])):
            worksheet1.write(i + 1, j, data_list[i][j])

    # 将xls文件保存到你给定的路径。
    workbook.save(storage_location_xls)
    print("The file is successfully saved in .xls format.")
    print(f"You can find it in the following path:\n{storage_location_xls}")
    print()


def store_data_db(storage_location_db, data_list):
    # 先与给定路径的数据库创立连接，如果不存在则新建一个数据库。
    conn = sqlite3.connect(storage_location_db)
    # 在数据库中创建一个光标，sql语句通过这个光标进行输入。
    c = conn.cursor()

    # 在数据库中创建一个命名为douban_films_top250的表格。
    # 通过如下SQL命令创建表格中的字段名，字段名的类型和属性。
    sql = '''
    create table if not exists douban_films_top250(
        中文名 text primary key,
        原名 text not null,
        主创人员 text not null,
        类型 text not null,
        评分 float not null,
        评分人数 int not null,
        介绍 text not null,
        链接 text not null,
        封面 text not null);'''

    # 将sql语句通过光标写到了conn里，再执行到数据库。
    c.execute(sql)

    for film in data_list:
        # 通过如下SQL命令向表格douban_films_top250中插入数据。
        sql = '''
        insert into douban_films_top250(中文名, 原名, 主创人员, 类型, 评分, 评分人数, 介绍, 链接, 封面)
        values(?, ?, ?, ?, ?, ?, ?, ?, ?);'''

        # 向SQL语句中的占位符?传入数据时，要用()括起来当作一个元组。
        c.execute(sql, (film[0], film[1], film[2], film[3], film[4], film[5], film[6], film[7], film[8]))

    # 在修改数据库后要确认修改，若只是查询就不用commit()了。
    conn.commit()
    # 使用数据库完毕后应关闭数据库，否则有泄漏的隐患。
    conn.close()
    print("The file is successfully saved in .db format.")
    print(f"You can find it in the following path:\n{storage_location_db}")
    print()


if __name__ == "__main__":
    main()
