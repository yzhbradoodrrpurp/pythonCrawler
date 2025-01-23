# -*- coding = utf-8 -*-
# @Time: 2024/9/17 14:07
# @Author: Zhihang Yi
# @File: 010regularExpression.py
# @Software: PyCharm
"""
这一章里，我们学习正则表达式(Regular Expression)。
所谓正则表达式，就是一种对字符串的模版规定。
"""
import re  # 引入一个正则表达式的库。

"""
正则表达式常用符：
.：表示任意单个字符(包括特殊字符，但不包括换行符\n)。
[...]：字符集，表示...中的任意单个字符。
[^...]：非字符集，表示任意非...中的单个字符。
*：前一个字符0次或无限次扩展。
+：前一个字符1次或无限次扩展。
?：前一个字符0次或1次扩展。
...|...：左右任意一个表达式。
{m}：扩展前一个字符m次。
{m, n}：扩展前一个字符m～n次(包含n次)。
^...：表示一定要以字符串...为开头。
...$：表示一定要以字符串...为结尾。
(...)：分组标记，表示将字符串...作为一个整体来看待。
\d：表示所有单个数字，等同于[0-9]。
\w：表示任意单个字母、数字、下划线。
"""

pattern = re.compile("AAA")  # compile()函数用于创建一个模版，然后判断其它字符串符不符合这个标准。
match_or_not = pattern.search("ABBBAAAA")  # search()用于比对是否含有模版中的字符串，没有的话显示None。
print(match_or_not)

# 也可以用一句话来比对，AAA依旧是模版，ABBBAAAA就是要比对的对象。
match_or_not = re.search("AAA", "ABBBAAAA")
print(match_or_not)

# findall()函数接收一个模版和一个被比较的对象，返回一个列表，不匹配时返回一个空列表。使用方法其实和search()相同。
pattern = re.compile("a")
all_a = pattern.findall("abaabbbc")
print(all_a)  # 列表内容的类型为str。

all_a = re.findall("a", "abaabbbc")
print(all_a)

capitalLetter = re.findall("[A-Z]+", "AAPbCdESGfGhIjKlMONOp")
print(capitalLetter)

# sub()函数可以将在一串字符串中将某些字符串替代为另一些字符串。
# 这里是将所有的a全都替换为A。
print(re.sub("a", "A", "appMozart"))
