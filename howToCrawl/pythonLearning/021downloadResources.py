# -*- coding = utf-8 -*-
# @Time: 2024/10/3 18:52
# @Author: Zhihang Yi
# @File: 021downloadResources.py
# @Software: PyCharm

import urllib.request
from bs4 import BeautifulSoup
import re


def main():
    basic_url = 'https://movie.douban.com/top250'
    starting_page = int(input('Enter the starting page: '))
    ending_page = int(input('Enter the ending page: '))

    # https://movie.douban.com/top250?start=25&filter=
    for page in range(starting_page, ending_page + 1):
        if page == 1:
            url = basic_url
        else:
            url = basic_url + '?start=' + str((page-1)*25) + '&filter='

        picture_list = crawl_webpage(url)
        download_pictures(picture_list)
        print(f"The {page}th page has been downloaded.")

    print("All execution is done.")


def crawl_webpage(url):
    headers = {
        'Cookie':
            'Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1727953243; '
            'Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1727152265,1727952856; '
            '_clsk=sosocn%7C1727952865574%7C2%7C1%7Cv.clarity.ms%2Fcollect; '
            '_clck=1xolgoa%7C2%7Cfpp%7C0%7C1728; HMACCOUNT=B423DEE5327D9D22; '
            'cz_statistics_visitor=1e0b14cc-2c48-d547-e96b-4777f8d5bb51',
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 '
            'Safari/605.1.15'
    }

    try:
        req = urllib.request.Request(url=url, headers=headers)
        handler = urllib.request.HTTPSHandler
        opener = urllib.request.build_opener(handler)
        response = opener.open(req)
    except Exception as e:
        print(e)

        return []
    else:
        picture_list = parse_data(response.read().decode('utf-8'))

        return picture_list


def parse_data(content):
    soup = BeautifulSoup(content, 'html.parser')
    pictures_info = soup.find_all(name='div', class_='pic')

    # src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg"
    picture_pattern = re.compile(r'src="(.*?)"')
    # alt="肖申克的救赎"
    name_pattern = re.compile(r'alt="(.*?)"')

    picture_list = []

    for picture_info in pictures_info:
        picture = picture_pattern.findall(str(picture_info))[0]
        name = name_pattern.findall(str(picture_info))[0]

        picture_list.append([name, picture])

    return picture_list


def download_pictures(picture_list):
    for picture in picture_list:
        # urlretrieve()是一个用于从指定url下载文件的函数，第一个变量是资源的url，第二个变量是资源储存的路径和名字。
        urllib.request.urlretrieve(url=picture[1], filename='/Users/yzhbradoodrrpurp/Desktop/douban_films_top250_imgs/' + picture[0] + '.jpg')


if __name__ == '__main__':
    main()
