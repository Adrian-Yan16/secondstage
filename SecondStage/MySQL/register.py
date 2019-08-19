"""
将注册信息存入数据库
"""
import pymysql


class DictDatabase:
    def __init__(self,name,password):
        self.__connect_database()
        self.__name  = name
        self.__password = password

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

    def register(self):
        sql = "insert into user values (%s,%s);"
        try:
            self.cur.execute(sql,[self.__name,self.__password])
            self.db.commit()
        except Exception:
            self.db.rollback()
            return  False
        return True

    def login(self):
        while True:
            sql = "select name,password from user;"
            self.cur.execute(sql)
            for item in self.cur.fetchall():
                if self.__name == item[0]:
                    if self.__password == item[1]:
                        return True
                    else:
                        return False
            return False

if __name__ == '__main__':
    r_l = int(input("注册输入1，登录输入2"))
    name = input("name:")
    password = input("password:")
    dd = DictDatabase(name,password)
    if r_l == 1:
        if dd.register():
            print("注册成功")
        else:
            print("注册失败")
    else:
        if dd.login():
            print("登录成功")
        else:
            print("登录失败")
