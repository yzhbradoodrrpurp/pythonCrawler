# -*- coding = utf-8 -*-
# @Time: 2024/9/27 16:29
# @Author: Zhihang Yi
# @File: 017selenium3.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 设置无头模式
chrome_options = Options()
chrome_options.add_argument("--headless")

# 启动无头浏览器
driver = webdriver.Chrome(options=chrome_options)

# 打开网页
driver.get("https://google.com")

# 获取网页标题
print(driver.title)

# 获得一张截图，以证明无头浏览器确实打开过。
driver.save_screenshot('GoogleFrontPage.png')

# 关闭浏览器
driver.quit()
