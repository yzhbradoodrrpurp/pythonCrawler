# -*- coding = utf-8 -*-
# @Time: 2024/9/12 10:36
# @Author: Zhihang Yi
# @File: 001JanKenPunch.py.py
# @Software: PyCharm

"""
这是一个石头剪刀布游戏，
0代表石头，1代表剪刀，2代表布。
"""
import random

while True:
    print("Enter a number between 0 and 2:", end=" ")
    randomNum = random.randint(0, 2)
    yourNum = int(input())

    if yourNum < 0 or yourNum > 2:
        print("You've entered a wrong number.")
    else:
        if yourNum == 0:
            if randomNum == 0:
                print("No one wins.")
            elif randomNum == 1:
                print("You win.")
            elif randomNum == 2:
                print("You lose.")
        elif yourNum == 1:
            if randomNum == 0:
                print("You lose")
            elif randomNum == 1:
                print("No one wins.")
            elif randomNum == 2:
                print("You win.")
        elif yourNum == 2:
            if randomNum == 0:
                print("You win")
            elif randomNum == 1:
                print("No one lose.")
            elif randomNum == 2:
                print("No one wins.")
