# -*- coding = utf-8 -*-
# @Time: 2024/9/14 12:39
# @Author: Zhihang Yi
# @File: 005function.py
# @Software: PyCharm

def rank_up(num_list):  # Python中的函数定义要用def，大概的形式和C中相似。函数的定义没有特定的位置，不过一般推荐在开头。
    times = 0

    while times < len(num_list):
        max_id = 0

        for i in range(1, len(num_list) - times):
            if num_list[i] > num_list[max_id]:
                max_id = i

        mid = num_list[max_id]
        num_list[max_id] = num_list[len(num_list) - times - 1]
        num_list[len(num_list) - times - 1] = mid
        times += 1


def search(num_list, content):  # Python中的函数可以接受单个变量，也可以接受多个变量，也可以不接受变量，这一点和其它高级语言一样。
    for i in range(len(num_list)):
        if content == num_list[i]:
            return "'{}' exists in the list.".format(content)  # Python可以返回值，类型无所谓；也可以不返回值，则默认return None。

    return "'{}' doesn't exist in the list.".format(content)


def sum_and_average(num_list):
    summary = 0

    for i in range(len(num_list)):
        summary += int(num_list[i])

    average = summary / len(num_list)

    return summary, average  # 可以返回多个值，用逗号分隔，整体上是一个元组，也可以用相应个变量进行接收。


num_list = list(input("Enter several numbers separated by space: ").split())  # split()函数识别输入的多个内容，默认分隔是空格。
rank_up(num_list)
print("The ascending order of the list: %s." % num_list)

content = int(input("Enter a number you want to look for:"))
print(search(num_list, content))

summary, average = sum_and_average(num_list)
print(sum_and_average(num_list))
print(summary, average, sep=", ")


"""
Python程序入口点：
if __name__ == "__main__":  __name__是Python中的内置变量，类型为str。
当一个Python文件直接被执行时，__name__的值是__main__；当这个文件作为一个模块导入到其它文件中时，__name__的值是这个模块的名字(比如：005function)。
"""
def main():
    pass


if __name__ == "__main__":  # 整个代码块的意义是，如果直接执行这个Python文件，则调用main()函数。
    main()  # 值得注意的是，Python并没有像C一样强制要求有一个main函数，但是可以自己定义。
