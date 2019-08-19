"""
单词查找
"""

import pymysql

class QueryWord:
    def __init__(self,word):
        self.__word = word

    def __connect_database(self):
        # 建立连接
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             passwd="123456",
                             database="dict",
                             charset="utf8")
        #创建游标对象
        cur = db.cursor()
        return db,cur

    def find_annotation(self):
        db,cur = self.__connect_database()
        sql = "select annotation from words where word = '%s';"%self.__word
        cur.execute(sql)
        db.commit()
        annotation = cur.fetchone()
        cur.close()
        db.close()
        return annotation


if __name__ == '__main__':
    word = input("请输入要查询的单词：")
    query = QueryWord(word)
    annotation = query.find_annotation()
    print("注释为",annotation)

