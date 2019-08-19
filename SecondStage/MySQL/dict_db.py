"""
将单词存入words单词表，单词及注释存入不同的字段 （超过19500即可）
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
                             database="dict",
                             charset="utf8")
        # 创建游标对象
        self.cur = self.db.cursor()


    def insert_data(self):
        f = open("dict.txt")
        sql = "insert into words (word,annotation) values (%s,%s);"
        pattern = re.compile(r"(\S+)\s+(.*)")
        for line in f:
            if not line:
                print("字典导入完成")
                return
            tup = pattern.findall(line)[0]
            try:
                self.cur.execute(sql,tup)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
        self.cur.close()
        self.db.close()

dd = DictDatabase()
dd.insert_data()


