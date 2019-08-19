"""
将二进制文件从数据库中取出
"""
import pymysql


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

    def get_data(self):
        sql = "select image from class_1 where id = 1;"
        self.cur.execute(sql)
        with open("小姑娘.jpg", "wb") as f:
            f.write(self.cur.fetchone()[0])
        self.cur.close()
        self.db.close()


dd = DictDatabase()
dd.get_data()
