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

#写数据库
try:
    # name = input("name:")
    # age = input("age:")
    # score = input("score:")
    #插入
    #sql = "insert into class_1 (name,age,score) values (%s,%s,%s);"
    #cur.execute(sql,[name,age,score])               #列表只能给values后的值传入

    #修改
    # sql = "update interest set price = 5000 where price < 5000"
    # cur.execute(sql)

    #删除
    sql = "delete from marathon where name like '王_' limit 1;"
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
    print(e)
cur.close()
db.close()