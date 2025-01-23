# -*- coding = utf-8 -*-
# @Time: 2024/9/14 16:22
# @Author: Zhihang Yi
# @File: 006fileutil2.py
# @Software: PyCharm

"""
有时候需要对文件进行重命名、删除等操作，
这个时候就需要import os。
os模块是Python中自带的一个模块。
"""
import os

# 第一个位置是原来的文件名，第二个位置是要改成的文件名。
# 如果原来的文件名不存在，则会报错。
os.rename('testFile.txt', 'test.txt')

os.remove('test.txt')  # 删除名为test.txt的文件，如果不存在也会报错。

# ... 也有其它的函数，可以问ChatGPT自行了解。

