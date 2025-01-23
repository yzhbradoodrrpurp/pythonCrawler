# -*- coding = utf-8 -*-
# @Time: 2024/9/26 20:37
# @Author: Zhihang Yi
# @File: 017selenium2.py
# @Software: PyCharm

from selenium import webdriver
import time

def main():
    """
    做法和selenium1一摸一样，只是这次我们该用Chrome，便于使用无头浏览器。
    由于我已经将chromedriver添加到了环境变量中，所以不需要配置路径了。
    """
    driver = webdriver.Chrome()
    driver.get('https://google.com')

    time.sleep(2)

    driver.quit()


if __name__ == '__main__':
    main()
