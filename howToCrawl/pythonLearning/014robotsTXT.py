# -*- coding = utf-8 -*-
# @Time: 2024/9/23 19:18
# @Author: Zhihang Yi
# @File: 014robotsTXT.py
# @Software: PyCharm

import urllib.robotparser

def main():
    # 查看的网站。
    basic_url = "https://www.flightradar24.com"
    # 用户代理，表明你从哪里访问。
    user_agent = ("Mozilla/5.0 (Macintosh; "
                  "Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15")

    # 创建了一个名为rp的RobotFileParser对象。
    rp = urllib.robotparser.RobotFileParser()
    # 为rp设定了一个访问的url的robots.txt。
    rp.set_url(basic_url + "/robots.txt")
    # 解析得到的robots.txt。
    rp.read()
    # 检查能否爬取https://movie.douban.com下的top250页面。
    can_fetch = rp.can_fetch(user_agent, basic_url + "/")

    print(can_fetch)


if __name__ == '__main__':
    main()
