# -*- coding = utf-8 -*-
# @Time: 2024/9/12 15:16
# @Author: Zhihang Yi
# @File: 002iterableTypes2.py
# @Software: PyCharm

"""
创建字符串时可以用单引号也可以用双引号。
字符串也是可以迭代的对象，索引、切片、追加功能也能用。
但是append, insert, del, pop, remove无法使用。
"""
j = "Hello World!"
print(j[0], j[-1])
print(j[1:3])
j += " Let's go to hell!"
j += " Wow..."*2  # 即Wow...追加两次。
print(j)

print("{} is a kind of {}.".format("Bird", "animal"))  # {}是占位符号，.format(..., ...)跟在字符串后面，内容用来代替占位符。
print("{2} is in {0} while {3} is in {1}.".format("China", "America", "Shanghai", "New York"))  # 可以用数字来标注要替代的位置。

longStr = '''
I happened to meet a girl in Osaka and quickly fell in love with her.
Despite not knowing her name and phone number at all, I've been haunted by her figure and smile all night long. 
'''
print(longStr)  # '''三个单引号用于多行的字符串。


"""
set即集合，特点是没有顺序且变量的值是唯一的。
"""
k1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # set的定义用{}；tuple的定义用()；list的定义用[]。
h = [2, 3, True, "Yep"]
k2 = set(h)  # set(...)接收一个列表并将它转化为集合。
k1.add(2)  # 无效语句，因为2已经在集合中存在了。
k1.update(k2)  # 括号中填入任何一个可迭代的对象，list, tuple, str, set都可以，将这个对象添加到集合中。

k1.discard(2)  # discard()函数是集合类型set专属的。
k1.remove("Yep")  # discard()和remove()都是一样的功能，删除一个内容。区别在于若这个内容不存在，则discard不会报错，而remove会报错。
k1.clear()  # 作用是清空集合k1中的内容，可作用于集合和字典。
print(k1)

k1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(k1.union(k2))  # 取k1, k2集合的并集。
print(k1.intersection(k2))  # 取k1, k2集合的交集。
print(k1.difference(k2))  # 在k1中但不在k2中的元素集合。
print(k1.symmetric_difference(k2))  # 只在k1或者k2中的元素集合。


"""
dict即字典，是无序对象的集合，使用键值(key-value)存储，和Java中的map是类似的。
dict的作用是可以通过键查找到值，所以同一个字典中，键的值是唯一的。
"""
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
print(dict1["a"], dict1["b"], dict1["c"], sep=" ")  # 访问dict中的值需要通过键和[]，与list, tuple类似，值得注意的是，当键不存在时会报错。
print(dict1.get("a"), dict1.get("b"), dict1.get("c"), sep=" ")  # 通过get()函数访问，当键不存在时不会报错，而是输出None。
print(dict1.get("d", "The key doesn't exist."))  # 用get()函数访问时可以加上一个默认返回值，当键不存在时则返回默认值。

dict1["c"] = 4  # 可以直接通过添加一个新的键来添加一个键值对。
print(dict1)

del dict1["a"]  # 和list,tuple类似，del可以删除一个键值对，也可以删除整个dict。
deletedValue = dict1.pop("c")  # 类似的，也可以用pop进行弹出。
print(deletedValue)

dict1["a"] = 1
dict1["c"] = 3

print(dict1.keys())  # dict1.keys()可以访问dict1字典中的每一个键。
for key in dict1.keys():
    print(key)

print(dict1.values())  # dict1.values()可以访问dict1字典中的每一个值。
for value in dict1.values():
    print(value)

print(dict1.items())  # dict1.items()可以访问每一个键值对，每个键值对以元组的形式出现。
for item in dict1.items():
    print(item)

for key, value in dict1.items():  # 由于items()得到的是一个键值对元组，那么就包含两个内容，可以分别赋给key和value。
    print("%s-%s" % (key, value))

# dict的其它创建方式：
dict2 = dict([["name", "Joshua"], ["age", 19], ["location", "Boston"]])
dict3 = dict([("name", "Joshua"), ("age", 19), ("location", "Boston")])  # 这两种方法实际上是通过类型转换，将list, tuple转化为dict。
dict4 = dict(name="Joshua", age=19, location="Boston")  # 创建多个变量并赋值，然后类型转化为dict。

# 可迭代变量list, tuple, set, dict都可以用%s进行输出。
