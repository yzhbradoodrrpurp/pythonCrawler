# -*- coding = utf-8 -*-
# @Time: 2024/9/14 14:32
# @Author: Zhihang Yi
# @File: 005FunctionPractice.py
# @Software: PyCharm

def print_a_line():
    print("-"*30)


def print_several_line(x):
    for i in range(x):
        print_a_line()


def summary(num_list):
    summary = 0

    for i in range(len(num_list)):
        summary += int(num_list[i])

    return summary


def average(num_list):
    return summary(num_list) / len(num_list)


print_a_line()

x = int(input("How many row of lines do you want:"))
print_several_line(x)

num_list = list(input("Enter three numbers:").split())
print(summary(num_list))
print(average(num_list))
