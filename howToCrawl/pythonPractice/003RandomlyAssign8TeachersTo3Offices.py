# -*- coding = utf-8 -*-
# @Time: 2024/9/12 15:19
# @Author: Zhihang Yi
# @File: 003RandomlyAssign8TeachersTo3Offices.py
# @Software: PyCharm

import random

offices = [[], [], []]
teachers = ["Alice", "Bob", "Chris", "Denis", "Eddie", "Frank", "Grace", "Harry"]

for teacher in teachers:
    office = random.randint(0, 2)
    if office == 0:
        offices[office].append(teacher)
    elif office == 1:
        offices[office].append(teacher)
    elif office == 2:
        offices[office].append(teacher)

for officeID in range(len(offices)):
    if offices[officeID]:  # 当一个列表是非空的时候，返回True；当一个列表是空的时候，返回False。
        print("For the {}th office, the faculty is {}.".format(officeID + 1, offices[officeID]))
    else:
        print("For the {}th office, the faculty is none.".format(officeID + 1))
