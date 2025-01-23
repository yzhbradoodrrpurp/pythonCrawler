# -*- coding = utf-8 -*-
# @Time: 2024/9/12 09:47
# @Author: Zhihang Yi
# @File: 002iterableTypes1.py
# @Software: PyCharm

import fractions

"""
Python中没有原生数组类型，只有list类型。
list类型的长度是动态的，从0开始计数，可以像数组一样用h[i]来访问第i个变量。
同时可以用负数从末尾来访问，h[-1]就表示最后一个变量，h[-2]表示倒数第二个变量。
"""
h = [1, 2, 3, 4, 5]  # list的一般赋值方式。
h[0], h[1], h[2] = 99, 32, 45  # 用h[i]的方式访问第i个变量。

print(h)  # list的一般输出方式。
print(h[2:5])  # 输出h中从2到5(不包括5)位置的变量。
print(h[:5])  # 如果是从第一位开始输出，那么可以省略。
print(h[2:])  # 如果是输出到最后一个数值，那么也可以省略。、
print(h[:])  # 首尾全都省略，即输出整个链表。

h = h[::2]  # 也是首尾省略了，2表示从第0个开始，每隔两个位置取一个变量，即取出偶数位上的变量。
h = h[::-1]  # 同样省略了首尾，表示倒着取出首尾的变量。

h += [34]  # 即h = h + [34], 在列表h的末尾追加34。
h += [fractions.Fraction(5, 8)]
h += [True]
h += ["String"]  # 一个列表中的变量的类型不是唯一的，可以追加其他类型的变量。
print(h)

h.append('a')  # 追加的另一种方式。
h.insert(2, 6 + 7j)  # 在第2个位置上插入6 + 7j，原来第2个位置及以后的变量都向后移动一位。
h.extend([1, 2, 3])  # extend(...)中的...是一个列表，将这个列表追加到h的末尾，这同样也可以用append完成。

del h[0]  # 表示删除列表第0个位置上的数值。也可以del h删除整个列表，此时h不存在了。
h.remove(4)  # remove(...)中接收一个内容，删除列表中第一次出现的这个内容，若不存在则会引发valueError。
h.pop()  # 如果pop.(...)中不接受任何数值的话，则删除最后一个变量并返回这个变量；如果接收一个数值i的话，则删除第i个变量并返回这个变量。
print(1 in h)  # 检查内容1是否在h列表中，返回一个bool类型。
print(h.index(2))  # 返回第一次出现内容2的索引，如果不能存在则会引发valueError。
print(h)

# 列表也可以像C中的数组一样定义成多维的，每一个维度的长度可以不同。
schoolNames = [["SCU", "UESTC"], ["PKU", "THU", "RUC"], ["Stanford", "UC Berkeley", "MIT", "CMU"]]
print(schoolNames[0][0])  # SCU
print(schoolNames[0][1])  # UESTC
print(schoolNames[2][1])  # UC Berkeley


"""
元组tuple和list相似，唯二的区别在于赋值时用的是()，访问时依然用[]，定义后不可修改。
list能用的功能，tuple基本都能用。
"""
i = (1,)  # 当元组里只有一个内容时，必须在末尾加上一个,，否则Python会将它误读为：i = (1)，即i=1，i实际上时int。
i = (1, 2, 3, 4)
print(2 in i)  # 检查2是否在i中，返回一个bool类型。
print(i.index(4))  # 返回第一次出现内容4的索引，如果不存在则会引发valueError。
print(i.index(4, 0, 3))  # 查找指定范围1～3(不包括3)内有没有内容4，有的话则返回索引，没有的话则valueError。
