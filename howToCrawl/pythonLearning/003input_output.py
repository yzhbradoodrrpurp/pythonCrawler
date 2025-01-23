# -*- coding = utf-8 -*-
# @Time: 2024/9/11 23:30
# @Author: Zhihang Yi
# @File: 003input_output.py
# @Software: PyCharm

import random

print("{} is a kind of {}.".format("Bird", "animal"))  # {}是占位符号，.format(..., ...)跟在字符串后面，内容用来代替占位符。
print("{2} is in {0} while {3} is in {1}.".format("China", "America", "Shanghai", "New York"))  # 可以用数字来标注要替代的位置。

nation = "China"
name = "Zhihang Yi"
print("I'm from %s." % nation)  # 和C语言类似，%d整数，%f浮点数，%c字符，%s字符串。
print("I'm %s and from %s." % (name, nation))  # 用两个占位符时，后面也只用一个%，但是括起来两个变量。

print("www", "baidu", "com", sep=".")  # sep表示不同内容之间的分割，如果不写的话默认是一个空格。
print("aaa", "bbb", "ccc", sep="\n")  # \n的作用和C, Java中一致，表示换行符。

print("Hello World!", end=" ")
print("It's a nice day!", end=" ^_^\n")  # end表示这一行以什么结尾，不加的话默认是\n换行符。

password = input("Enter the password:")  # Python中的输入用input(...)，里面的内容是提示词。
print("The password is %s." % password)
print("{} is the password.".format(password))


x = random.randint(3, 45)  # 随机生成一个3～45的数(包含边界)，需要import random。
print("{} is the randomly-generated number.".format(x))


# \是转义字符，用于保留字符的特定功能，\n, \t的作用和C, Java中的类似。
print("Chengdu\nHello!")
print(r"Chengdu\nHello!")  # 在字符串前面加上一个r，表示字符串中所有的转义字符不发挥作用，而是直接显示出来。
