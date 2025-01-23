# -*- coding = utf-8 -*-
# @Time: 2024/9/14 18:46
# @Author: Zhihang Yi
# @File: 007exceptionHandling.py
# @Software: PyCharm

try:
    f = open('exceptionHandling.txt', 'r')  # 异常处理，try里面放置可能出现异常的代码。
except FileNotFoundError:  # 错误类型必须要和报错中的错误相匹配，通常就直接从报错里复制过来。
    print("The file doesn't exist.")


try:
    f = open('exceptionHandling.txt', 'r')
    print(num)
except (FileNotFoundError, NameError):  # 可以将错误类型组成一个元组(只能用元组)，这样可以捕捉多种异常。
    print("There has been an error or two.")


try:
    f = open('exceptionHandling.txt', 'r')
    print(num)
except FileNotFoundError:  # 也可以用多个except语句来捕捉多种异常。
    print("The file doesn't exist.")
except NameError:
    print("The variable hasn't been defined yet.")


try:
    f = open('exceptionHandling.txt', 'r')
    print(num)
except (FileNotFoundError, NameError) as errorInfo:  # 可以用as将异常对象储存为errorInfo，方便下文中打印出具体的异常。
    print("There's been an error: {}".format(errorInfo))  # 值的注意的是，errorInfo的类型不是str，所以不能用%s输出。


try:
    f = open('exceptionHandling.txt', 'r')
    print(num)
except Exception as errorInfo:  # 可以用Exception指代所有的异常类型。
    print("There's been an error: {}".format(errorInfo))


# 整个异常处理的结构如下：
try:  # try里面放可能引发异常的代码。
    f = open('exceptionHandling.txt', 'r')
    print(num)
except Exception as errorInfo:  # except要对应异常类型，except里面放置发生异常时执行的代码。
    print("There's been an error: {}".format(errorInfo))
else:  # else里面放置没有发生异常时执行的代码。
    print("There is no error.")
finally:  # finally里面放置无论发没发生异常最终都会执行的代码。
    print("The whole execution is done.")
