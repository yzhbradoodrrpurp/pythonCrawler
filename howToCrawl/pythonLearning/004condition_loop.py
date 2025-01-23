# -*- coding = utf-8 -*-
# @Time: 2024/9/12 10:00
# @Author: Zhihang Yi
# @File: 004condition_loop.py
# @Software: PyCharm

"""
Python中也有条件语句，关键词是if, elif, else。
但是Python中的条件结构不需要用(){}括起来，而是以一个冒号进行结尾，以缩进作为语句块。
Python是强制缩进的。
Python中没有switch-case语法结构。
"""
a = int(input("assign a number to a:"))  # input的内容实际上是str，需要进行类型转换才能当成int。

if a > 0:
    print("Positive.")
elif a < 0:
    print("Negative.")
else:
    print("0")

print("End.")  # 如果要跳出if语句，则只用和if-else处于相同的缩进位。

score = int(input("Enter your score: "))

if score <= 100 and score >= 90:  # Python用and, or表示&&, ||。Python支持连续比较，可以写为： 90 <= score <=100。
    print("Your grade is A.")
elif score >= 85:
    print("Your grade is A-.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 75:
    print("Your grade is B-.")
else:
    print("Your grade is C.")


# range(..., ..., ...)函数接收3个数值，起始值，结束值(不包括结束值)，间隔值。起始值不写则默认为0，间隔值不写则默认为1.
for i in range(5):
    if i != 4:
        print(i, end=", ")
    else:
        print(i)

for i in range(5, 30, 3):
    if i != 29:
        print(i, end=", ")
    else:
        print(i)


# in后面不仅可以跟数字，还可以跟上其它类型的变量。
l = ["aaa", "bbb", "ccc", "ddd"]

for item in l:
    print("%s is in the list." % item)

for item in ["aaa", "bbb", "ccc", "ddd"]:
    print(item, end=" ")

print()

for i in range(len(l)):  # len(...)函数得到长度，range(...)不包含末尾的值。
    print("The %dth item is %s." % (i, l[i]))

for char in "Chengdu":  # for循环可以对任何一个可迭代的对象进行操作，list, tuple, set, str, dic。
    print(char, end="")

print("\n")

# while的写法和for类似，都没有(){}且末尾要加上:。
i = 0

while i < 5:
    print("It's the %dth time to execute the loop." % (i+1))
    i += 1

# while可以和else连用，条件成立时在while中循环，不成立时执行else中的指令。

i = 0

while i < 5:
    print("It's the %d th time to execute the loop." % (i+1))
    i += 1
else:
    print("It's the end of the loop and i equals to %d." % i)

# break和continue在Python中的用法和在C, Java中的用法类似。
