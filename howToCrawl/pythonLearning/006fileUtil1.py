# -*- coding = utf-8 -*-
# @Time: 2024/9/14 15:20
# @Author: Zhihang Yi
# @File: 006fileUtil1.py
# @Software: PyCharm

"""
open()的作用是打开一个文件，如果不存在的话，会新建一个文件。
‘w'的意思是写入模式，如果文件存在且有内容的话，则会清空文件；
文件不存在的话，则会创建一个文件并使用写入模式。
如果'w'不存在时，则默认是'r'，意思是只读模式。
如果文件存在，只读模式正常运行；如果文件不存在，则会报错。
"""
f = open('test.txt', 'w')
f.write('''Hello World, I am new here!
What's your name?
I'd be quite glad to know about you!''')  # 用write()函数进行写入。
f.close()  # 关闭一个文件就是用close()函数。一个文件打开后必须关闭。


"""
可以注意到，在用只读模式打开一个文件后，文件指针从第一个字符开始扫描。
如果read()中不填入数字，则会读取从这个文件指针及以后的字符。
如果read()中填入数字n，则会读取这个文件指针及以后共n个字符。
"""
f = open('test.txt', 'r')
content = f.read(5)  # 打开只读模式后，用read()函数进行读取。
print(content)
content = f.read(5)
print(content)
content = f.read(5)
print(content)
f.close()
print()

f = open('test.txt', 'r')
content = f.read()
print(content)
f.close()
print()

"""
read()函数读取整个文件的内容，并将其作为单一的字符串返回。
readlines()函数读取整个文件的每一行，并将它们作为列表返回，列表的内容就是文件的每一行。
readlines()函数的括号中也可以规定读取的行数，原理和read()函数相似。
"""
f = open('test.txt', 'r')
content = f.readlines()
print(content)
f.close()
print()

# 因为readlines()返回的是列表，那么我们就可以用for循环对它进行一些操作。
f = open('test.txt', 'r')
content = f.readlines()
line_th = 1

for line in content:
    print("The %dth line: %s" % (line_th, line), end="")
    line_th += 1

f.close()
print("\n")


"""
readline()函数和read()函数类似，都是将内容作为字符串返回。
区别在于，readline()每次都只读取一行内容，即遇到换行符就结束读取。
"""
f = open('test.txt', 'r')

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1, line2, line3, sep="")

f.close()
print()
