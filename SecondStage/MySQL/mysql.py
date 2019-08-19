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

#执行sql语句
sql = "insert into class_1 values (8,'Emma',14,'w',78.3,'2019-8-8');"
cur.execute(sql)
db.commit()
cur.close()
db.close()