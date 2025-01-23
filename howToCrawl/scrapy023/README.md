# 1.创建Scrapy项目：
    在终端输入 'scrapy startproject ...' ...是文件名。 
    文件名只能以英文字母开头且文件名只能包含英文、数字、下划线。
    e.g.: scrapy startproject scrapy023


# 2.创建爬虫文件：
    必须在Scrapy项目下的文件夹spider文件夹下创建爬虫文件。
    在终端中输入 'scrapy genspider ... ...'  第一个...是文件的名称，第二个...是要爬取网站域名(不加上协议)。
    e.g.: scrapy genspider baidu_spider www.baidu.com


# 3.运行爬虫文件：
    只能在Scrapy项目的根目录下运行爬虫文件。
    在终端输入 'scrapy crawl ...' ...是要运行的爬虫文件的名字。
    e.g.: scrapy crawl baidu_spider


# 4.Scrapy项目的结构：
    scrapy023/
        scrapy023/
            __init__.py
            items.py
            middlewares.py
            pipelines.py
            settings.py
            spiders/
                __init__.py
        scrapy.cfg



 
