# -*- coding = utf-8 -*-
# @Time: 2024/10/4 19:46
# @Author: Zhihang Yi
# @File: 007starbucks_stores.py
# @Software: PyCharm

import urllib.request
import json
import sqlite3
import xlwt

def main():
    url = ('https://www.starbucks.com.cn/api/stores/nearby'
           '?lat=31.152616&lon=107.649879&limit=1000&locale=ZH&features=&radius=2640037')

    content = crawl_page(url)
    store_list = parse_json_data(content)
    store_data_db(store_list)
    store_data_xls(store_list)


def crawl_page(url):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15',
        'Cookie':
            'ZHh6ku4z=A-nYWFWSAQAAyB4uGRBRaCKOMuy2b1XzewOWRi0dRkBq-xmFp08f7JAqG1QwAdNTfgD6Ky9GwH9eCOfvosJeCA'
            '|1|0|73b2f86b9b9fded4fcfae7c44b957fa05df3e03e; ktlvDW7IG5ClOcxYTbmY=a; '
            'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219255597ac61a1c-01f5770b96a673f-3e62654b-189297'
            '0-19255597ac72d15%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbn'
            'RpdHlfY29va2llX2lkIjoiMTkyNTU1OTdhYzYxYTFjLTAxZjU3NzBiOTZhNjczZi0zZTYyNjU0Yi0xODkyOTcwLTE5MjU1NTk3YWM3'
            'MmQxNSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; sajssdk_2015_cross_new_user=1',
        'Referer':
            'https://www.starbucks.com.cn/stores/?features=&bounds=91.587868%2C12.621596%2C123.711891%2C49.683636',
        'Host':
            'www.starbucks.com.cn'
    }

    try:
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req, timeout=4)

        return response.read().decode('utf-8')
    except Exception as e:
        print(f'There\'s been an error:\n{e}')

        return []


def parse_json_data(content):
    content = json.loads(content)
    stores = content['data']

    store_list = []

    for store in stores:
        store_list.append([store['name'], store['address']['streetAddressLine3'], store['id']])

    print('Data is successfully parsed.')

    return store_list


def store_data_db(store_list):
    conn = sqlite3.connect('/Users/yzhbradoodrrpurp/Desktop/starbucks_stores.db')
    c = conn.cursor()

    sql = '''
    create table if not exists starbucks_stores(
    店铺名称 text primary key,
    店铺地址 text not null,
    店铺编号 text not null
    );'''

    c.execute(sql)

    for store in store_list:
        sql = '''
        insert into starbucks_stores(店铺名称, 店铺地址, 店铺编号)
        values(?, ?, ?);'''

        c.execute(sql, (store[0], store[1], store[2]))

    conn.commit()
    conn.close()

    print('Data is successfully stored in database.')


def store_data_xls(store_list):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet1 = workbook.add_sheet('starbucks_stores')

    sheet1.write(0, 0, '店铺名称')
    sheet1.write(0, 1, '店铺地址')
    sheet1.write(0, 2, '店铺编号')

    for i in range(len(store_list)):
        for j in range(len(store_list[i])):
            sheet1.write(i + 1, j, store_list[i][j])

    workbook.save('/Users/yzhbradoodrrpurp/Desktop/starbucks_stores.xls')

    print('data is successfully stored in Excel.')


if __name__ == '__main__':
    main()
