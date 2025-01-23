# -*- coding = utf-8 -*-
# @Time: 2024/9/12 13:10
# @Author: Zhihang Yi
# @File: 002MultiplicationTable.py
# @Software: PyCharm

for a in range(1, 10):
    for b in range(1, a+1):
        print("%d*%d=%d" % (a, b, a*b), end=" ")
    print()

a = 0

while a <= 9:
    b = 1
    while b <= a:
        print("%d*%d=%d" % (a, b, a*b), end=" ")
        b += 1
    a += 1
    print()
