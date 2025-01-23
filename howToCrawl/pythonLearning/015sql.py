# -*- coding = utf-8 -*-
# @Time: 2024/9/24 19:08
# @Author: Zhihang Yi
# @File: 015sql.py
# @Software: PyCharm

# 引入一个数据库的模块。
import sqlite3

def main():
    # 连接一个名为test.db的数据库，如果不存在则新建一个。
    conn = sqlite3.connect('test.db')
    # 创建一个光标，在光标里就可以执行sql语句。
    c = conn.cursor()

    """
    创建sql命令语句。
    create table company 创建了一个名为company的表格。
    ()里是表格每一列开头的内容。
    第一个变量是开头的名称，第二个是类型，primary key表示主键，not null表示不能为空。
    每个主键值在表中必须是唯一的且不能为空，确保没有两行数据会有相同的主键值。这使得每一行数据都可以被准确识别。
    """
    sql = '''
    create table company(
        id int primary key,
        name text not null,
        age int not null,
        address text not null,
        salary int not null);'''
    # 注意：表格在创建过后，相应的sql语句就应该删除了，否则会重复创建。

    # 对光标输入sql语句，实际上写到了连接对象conn里面。
    c.execute(sql)
    # 对连接对象conn使用commit()函数会将数据提交给数据库。
    conn.commit()
    # 关闭连接对象和数据库的连接。
    conn.close()

    # ------------------------------------

    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    """
    \insert into ...(...) 表示对表格...进行插入，括号中的是表格包含的字段名。
    values()括号中的就是一一对应的插入的内容。
    不同的行要用,相隔，结束时要在末尾加上;。
    """
    sql = '''
    insert into company(id, name, age, address, salary)
    values(001, "Bruce", 19, "Boston, MA", 19000),
        (002, "Bobby", 21, "San Francisco, CA", 21000),
        (003, "Jalen", 20, "Los Angeles, CA", 19000),
        (004, "Connor", 22, "New York, NY", 22000);'''
    # 注意：数据在添加过后，相应的sql语句就应该删除了，否则会重复添加。

    c.execute(sql)
    conn.commit()
    conn.close()

    # ------------------------------------

    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    # 从列表中查询相应的元素，sql语句如下。
    sql = "select id, name, age, address, salary from company"
    # 会返回一个类型为sqlite3.cursor的变量，对它使用fetchall()就得到了列表元素，赋给rows，里面包含了行数对应个元组，元组里是每一行各字段名对应的信息。
    rows = c.execute(sql).fetchall()

    for row in rows:
        print(row)

    # 也可以用*指代所有的字段名。
    sql = "select * from company"
    rows = c.execute(sql).fetchall()

    for row in rows:
        print(row)

    # 因为没有修改表格，所以并不用commit()函数。
    conn.close()

    # ------------------------------------

    info = [0o05, "Jason", 21, "Houston, TX", 17000]

    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    # 也可以用变量来传入参数，?作为占位符，传入的变量类型要和定义的字段名类型一致。
    sql = '''
    insert into company(id, name, age, address, salary)
    values(?, ?, ?, ?, ?);'''

    # 传入的参数要用()括起来当作一个元组来传入，元组内对应的变量去到对应的占位符?再去到对应字段名的列。
    c.execute(sql, (info[0], info[1], info[2], info[3], info[4]))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
