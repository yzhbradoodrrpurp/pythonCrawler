import pythonLearning
# pythonLearning是一个模块名，可以引入一整个模块。

from pythonLearning import test
# pythonLearning是一个模块名，test是这个模块里一个具体的对象(函数、类、变量名等)。

import fractions
# Python中注释单行用#，注释多行用"""。

"""
Python中几种常见的数据类型：
int, float, Fraction, complex, bool, list, tuple, str, set, dic。

Python不需要像C, C++, Java一样显性地定义变量类型，而是在使用时根据赋值的类型确定。
Python中的是一个弱类型语言，也就是说变量的类型是可以直接改变的。
"""
intNum = 100  # Python中每一行的末尾不需要加semicolon。
floatNum = 100.0  # Python中没有double类型变量，只有float类型。但Python中的float是64位的，和C中的double类型是一样的。
a, b, c = 1, 2.0, "Alice"  # Python一种特别的连续赋值方式。

d = fractions.Fraction(3, 4)  # Python中的分数表达方式，需要在开头import fractions。
e1 = complex(3, 4)  # Python中的虚数表达方式，即3+4i或3+4j。
e2 = 3 + 4j  # Python中另一种虚数的表达方式,其中j可以换成J。

f = 12345
f = "It's amazing"  # 直接改变f的类型在Python中是允许的。

g = True
g = False  # bool类型。


# type(...)的作用是得到一串关于...类型的字符串。
typeOfA = type(a)
typeOfB = type(b)
typeOfC = type(c)
typeOfD = type(d)
typeOfE1 = type(e1)
typeOfE2 = type(e2)
print(typeOfA, typeOfB, typeOfC, typeOfD, typeOfE1, typeOfE2)  # print()中加入逗号可以输出多个变量。


# Python中也可以进行强制类型转换，不过语法和C, C++, Java稍微有所不同。
numFromIntToFloat = float(intNum)
numFromFloatToInt = int(floatNum)
print(numFromIntToFloat, type(numFromIntToFloat))
print(numFromFloatToInt, type(numFromFloatToInt))


# Python中的数据运算：
a = 4 / 5  # Python中的/表示除法运算而不是整除运算，对除数和被除数没有要求，得到的结果是浮点数，这一点和C, Java不同。
b = 14 // 5  # Python中的//表示整除，对除数和被除数同样没有要求。
c = 34 % 4   # Python中的求余数和C, Java是类似的。
d = 4 ** 5  # **表示指数运算，即4的5次方。有另一种表达方式math.pow(..., ...)，不过需要import math。
