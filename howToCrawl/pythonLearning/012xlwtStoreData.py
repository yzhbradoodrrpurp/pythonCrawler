# -*- coding = utf-8 -*-
# @Time: 2024/9/19 22:48
# @Author: Zhihang Yi
# @File: 012xlwtStoreData.py
# @Software: PyCharm

# 引入一个处理Excel文件(.xls)的库。
import xlwt

def main():
    # 创建一个workbook对象，即Excel文件。
    workbook = xlwt.Workbook(encoding="utf-8")

    # 在这个文件中创建一个表单并命名，即worksheet。
    worksheet = workbook.add_sheet("sheet1")

    for i in range(0, 9):
        for j in range(0, i + 1):
            # 对这个表单中的格子进行输入，第一个空表示行，第二个空表示列，最后一个空表示内容。
            worksheet.write(i, j, "{}*{}={}".format(i + 1, j + 1, (i + 1)*(j + 1)))

    # 完成输入后应该保存文件，用save("...")函数，...是保存的名字。
    workbook.save("multiplication_table.xls")

    print("The whole execution is done.")


if __name__ == "__main__":
    main()
