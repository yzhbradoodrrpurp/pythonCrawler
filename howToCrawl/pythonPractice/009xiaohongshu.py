# -*- coding = utf-8 -*-
# @Time: 2024/10/6 12:45
# @Author: Zhihang Yi
# @File: 009xiaohongshu.py
# @Software: PyCharm

import urllib.request
from lxml import etree
import time
import sqlite3
import random


def main():
    url = 'https://www.xiaohongshu.com/explore'
    post_list = []

    try:
        while True:
            content = crawl_page(url)

            if content is not None:
                post = parse_data(content)

                if post is not None:
                    print(post)
                    post_list.append(post)
                else:
                    print("Oops, the post is unaccessible.")
                    continue
            else:
                print("You didn't obtain the webpage source code successfully.")
                continue

    except KeyboardInterrupt:
        print("You've stopped the program mannually.")

    store_data(post_list)


def crawl_page(url):
    headers = {
        'Cookie':
            'gid=yj8j0Yq0yjv8yj8j0YqjDxSSdq8YjE9q4EvjuqU01Whlu0q8vyW3ji8884JW4j48K8yd4D20; '
            'unread={%22ub%22:%2266ffee5b000000001902deef%22%2C%22ue%22:%2266fbeecb000000001a02375e%22%2C%22uc%22:21}; '
            'webBuild=4.36.5; xsecappid=xhs-pc-web; acw_tc=3e3cfabe4e201da26e9aafb916be0c685f23b4044b922ef7ff71571806a67ffe; '
            'sec_poison_id=07bac1f6-1e94-4689-b5f9-7156b65d5560; websectiga=82e85efc5500b609ac1166aaf'
            '086ff8aa4261153a448ef0be5b17417e4512f28; abRequestId=b20f9bd3cc74ae90e9400de982354eb5; '
            'access-token-creator.xiaohongshu.com=customer.creator.AT-68c5174158962322870031470ek0burot7rysqva; '
            'galaxy.creator.beaker.session.id=1726647893527092390758; '
            'galaxy_creator_session_id=rRAaO07xTaJCH8QAVp7kpMrOk6EBn7V32oUJ; '
            'x-user-id-creator.xiaohongshu.com=61252e2700000000010001ac; '
            'a1=192043b9ccaqunqrnbtni8a8di3odtpyqmqa4zy7130000399671; webId=b20f9bd3cc74ae90e9400de982354eb5; '
            'customerClientId=302829943133808; web_session=040069b0516d6f5651faa1bcb8344b5b941f1b',
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
            '(KHTML, like Gecko) Version/18.0 Safari/605.1.15'
    }

    req = urllib.request.Request(url=url, headers=headers)

    # proxies = proxy_pool()
    # handler = urllib.request.ProxyHandler(proxies=proxies)
    # opener = urllib.request.build_opener(handler)

    try:
        response = urllib.request.urlopen(req, timeout=4)
        # response = opener.open(req, timeout=4)
    except Exception as e:
        print("There's an error occurred.")
        print(e)
        return None
    else:
        print("You've successfully crawled into Xiaohongshu.")
        try:
            return response.read().decode('utf-8')
        except Exception as e:
            print("'Read()' function failed.")
            return None


def proxy_pool():
    proxy_pool = [
        {'https': '172.217.0.0'},
        {'https': '104.16.0.0'},
        {'https': '140.82.112.3'},
        {'https': '208.80.154.224'},
        {'https': '151.101.1.69'}
    ]

    num = random.randint(0, len(proxy_pool) - 1)

    return proxy_pool[num]


def parse_data(content):
    tree = etree.HTML(content)

    try:
        post = tree.xpath('//section[@class="note-item"]')[0]

    except IndexError:
        print("The post didn't appear for some reason.")
        return None
    else:
        words = post.xpath('//div[@class="footer"]//a[@class="title"]//span/text()')[0]
        author = post.xpath('//div[@class="footer"]//div[@class="author-wrapper"]//span/text()')[0]
        likes = post.xpath('//span[@class="count"]/text()')[0]

        return [words, author, likes]


def scroll_down(driver):
    driver.execute_script('window.scrollTo(0, window.innerHeight);')
    time.sleep(3)


def store_data(post_list):
    conn = sqlite3.connect('/Users/yzhbradoodrrpurp/Desktop/xiaohongshu_posts.db')
    c = conn.cursor()

    sql = '''
    create table if not exists xiaohongshu_posts(
    Content text primary key,
    Author text not null,
    Likes text not null 
    );'''

    c.execute(sql)

    for post in post_list:
        sql = '''
        insert or ignore into xiaohongshu_posts(Content, Author, Likes)
        values(?, ?, ?);'''

        c.execute(sql, (post[0], post[1], post[2]))

    conn.commit()
    conn.close()
    print("The information of posts has been stored in database.")
    print(f"You've obtained {len(post_list)} posts this time.")


if __name__ == '__main__':
    main()
