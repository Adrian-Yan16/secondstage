"""
将二进制文件存入数据库
"""
import pymysql
import re


class DictDatabase:
    def __init__(self):
        self.__connect_database()

    def __connect_database(self):
        # 建立连接
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  passwd="123456",
                                  database="stu",
                                  charset="utf8")
        # 创建游标对象
        self.cur = self.db.cursor()

    def insert_data(self):
        with open("小花.jpg", "rb") as f:
            data = f.read()
        sql = "update class_1 set image = %s where id = 1;"
        try:
            self.cur.execute(sql, [data])
            self.db.commit()
        except Exception:
            self.db.rollback()
        self.cur.close()
        self.db.close()


dd = DictDatabase()
dd.insert_data()
