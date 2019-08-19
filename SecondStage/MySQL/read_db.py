"""
基本流程
"""

import pymysql

#连接数据库
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "stu",
                     charset = "utf8")

#创建游标对象
cur = db.cursor()

#获取数据库数据
sql = "select * from class_1 where gender = 'm';"
cur.execute(sql)               #执行正确后cur调用函数获取结果

#获取一个查询结果
one_row = cur.fetchone()
print(one_row)                #元组

#获取多个结果
many_row = cur.fetchmany(3)
print(many_row)

#获取全部(获取结果为迭代获取，在上一次查询后开始）
all_row = cur.fetchall()
print(all_row)

#关闭数据库
cur.close()
db.close()