# -*- coding = utf-8 -*-
# @Time: 2024/9/26 12:21
# @Author: Zhihang Yi
# @File: 017selenium1.py
# @Software: PyCharm

"""
之前学的方法爬取静态网页是足够的了，但是在爬取一些动态网页就不行了。
在动态网页中，大量的信息不是静态地镶嵌在html语句中的，
而是使用了AJAX技术，通过JavaSCript获取JSON数据嵌套到html数据里的。
这也是为什么在爬取一些动态网页时，在html文件中找不到一些页面信息的原因。
这一讲我们学习selenium，它可以模拟人操作浏览器的行为。
"""

# webdriver是selenium模块中的一个对象，用于与浏览器的WebDriver建立连接并控制浏览器执行自动化操作。
# WebDriver是每个浏览器自带的特定程序，用于接收自动化工具的指令并执行相应的操作。
from selenium import webdriver
# By是一个通过类型定位元素的类，在find_element()中可以见到。
from selenium.webdriver.common.by import By


def main():
    # 在后台与Safari的SafariDriver建立连接。
    # 然后返回一个webdriver对象，赋值给driver。后续可以通过driver执行一些操作。
    driver = webdriver.Safari()

    # 通过driver可以打开一个url。
    driver.get("https://www.baidu.com")

    # 可以通过下面这个命令得到打开的url的标题。
    url_title = driver.title
    print(url_title)

    # 用quit()函数可以关闭整个浏览器。
    # 如果想再次使用，需要重新建立一个webdriver对象。
    driver.quit()

    # ----------------------------------

    driver = webdriver.Safari()

    driver.get("https://www.baidu.com")

    """
    webdriver有6种方式来定位元素，用find_element()函数来实现。
    
    六种方式分别是：
    ID(标签内的id属性), NAME(标签内的name属性), XPATH(类似于正则表达式的查询方式),
    TAG_NAME(标签名), CSS_SELECTOR(用bs4的语法来查询)。 
    注意大写。
    
    常用通过ID, NAME来查询。
    """
    # 在百度首页中通过定位名字的方式定位到了百度一下的按钮。
    # 第一个变量是确定查找方式，第二个变量是确定查找的内容。
    # 查找到的内容赋值给button，类型是网页元素(WebElement)。
    button = driver.find_element(by=By.ID, value='su')

    # ----------------------------------

    # 得到这个按钮对应的标签名。
    print(button.tag_name)
    # 得到百度一下这个按钮对应的标签里面的属性用get_attribute()函数。
    # 括号里面的内容是属性的名字，比如type, value, id, class等等。
    print(button.get_attribute('class'))
    # 获取这个按钮的元素文本(起始标签和结束标签之间的文本)。
    print(button.text)
    # 用click()函数点击这个网页元素。
    button.click()

    driver.quit()
    # -----------------------------------

    driver = webdriver.Safari()
    driver.get("https://www.baidu.com")

    # 获取搜索按钮的网页对象。
    button = driver.find_element(by=By.ID, value='su')
    # 获取文本框的网页对象，命名为textbox。
    textbox = driver.find_element(by=By.NAME, value='wd')

    # 在文本框中输入信息，就像你直接在百度文本框中查找信息一样。
    textbox.send_keys('周杰伦')
    # 点击百度一下按钮，就可以搜索周杰伦啦。
    button.click()

    # execute_script()函数是一个执行有效JavaScript代码的函数，代码放在()里打上双引号。
    # window.scrollTo()表示将页面滚动到指定的位置。
    # 第一个位置为0表示不进行水平滚动，第二个位置是进行垂直滚动的高度。
    # document.body.height是一个属性，用于获取整个网页的高度，确保可以滚动到整个页面的最底部。
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 用XPATH的方式查询next_page的网页对象
    next_page = driver.find_element(by=By.XPATH, value='//a[@class="n"]')
    next_page.click()

    # 打开了两个页面，第一个页面是搜索周杰伦后的页面，第二个页面是第二页。
    # back()函数能让你返回上一个页面，即第一个页面。
    driver.back()
    # forward()函数能让去去到下一个页面，即第二个页面。
    driver.forward()

    driver.quit()

    """
    注意：
    在调用 driver.quit()后，之前运行的 a = driver.find_element()中的a将不再有效。
    driver.quit()会关闭浏览器并释放与之相关的所有资源，导致之前的WebDriver实例失效。
    因此，任何通过该实例获取的元素(如a)都将变得不可用，尝试访问它们会引发异常。
    """


if __name__ == "__main__":
    main()
