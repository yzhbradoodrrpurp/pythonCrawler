# -*- coding = utf-8 -*-
# @Time: 2024/9/12 15:42
# @Author: Zhihang Yi
# @File: 004ProductTable.py
# @Software: PyCharm

products = [[[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []]]

for i in range(len(products)):
    if i == 0:
        products[i][0], products[i][1], products[i][2] = i, "iPhone", 6888
    elif i == 1:
        products[i][0], products[i][1], products[i][2] = i, "MacPro", 14800
    elif i == 2:
        products[i][0], products[i][1], products[i][2] = i, "Xiaomi", 2499
    elif i == 3:
        products[i][0], products[i][1], products[i][2] = i, "StarBucks", 31
    elif i == 4:
        products[i][0], products[i][1], products[i][2] = i, "Book", 60
    elif i == 5:
        products[i][0], products[i][1], products[i][2] = i, "Nike", 699

print("The item category is as follows:")

for i in range(len(products)):
    print(products[i])

code = input("Enter the code of the product. Press 'q' to quit:\n")
purchasedItems = []

while code != "q":
    code = int(code)
    purchasedItems.append(products[code])
    code = input()

print("The purchased items are as follows:")

for i in range(len(purchasedItems)):
    print(purchasedItems[i])
