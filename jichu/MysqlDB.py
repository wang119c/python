#!/usr/bin/python
# encoding=utf-8



# MySQL封装类方法2
import MySQLdb


# 定义一个类为My2的模块
class My2:  # 初始化连接属性

    user = ''
    host = ''
    passwd = ''
    data = {}

    def __init__(self, user, host, passwd):
        self.user = user
        self.host = host
        self.passwd = passwd

    # 连接数据库
    def connectDB(self):
        self.conn = MySQLdb.connect(user=self.user, host=self.host, passwd=self.passwd)  # 连接数据库
        print self.conn  # 查看数据库连接状态
        self.cur = self.conn.cursor()  # 连接游标
        print self.cur  # 查看游标连接状态

    # 选择库
    def selectDB(self):
        db_name = raw_input("please enter your db_name: ")
        self.conn.select_db(db_name)  # 选择库

    # 查询语句和数据库语句(show,dorp等简短的语句)
    def executeDB(self):
        while True:
            sql1 = raw_input("please enter your sql sentences: ")
            if sql1 == "q":
                break
            else:
                self.cur.execute(sql1)
                print self.cur.fetchall()
                # 以下均为数据操作的语句，包括insert,update,select,delete等
                # Insert语句

    def insertData(self, tablename, data):
        key = []
        val = []
        for i in range(len(data)):
            key.append(data.keys()[i])
            val.append("'" + str(data.values()[i]) + "'")
        key1 = ",".join(key)
        val1 = ",".join(val)
        sql = "insert into " + tablename + "(" + key1 + ") values (" + val1 + ")"
        return sql

    def inSert(self, tablename, data1):
        sql = self.insertData(tablename, data1)
        self.cur.execute(sql)

    # update语句
    def updateData(self, tablename, data, condition):
        val = []
        for i in range(len(data)):
            val.append(data.keys()[i] + "='" + str(data.values()[i]) + "'")
        val1 = ",".join(val)
        sql = "update " + tablename + " set " + val1 + " where " + condition
        return sql

    def upDate(self, tablename, data1, condition):
        sql = self.updateData(tablename, data1, condition)
        self.cur.execute(sql)

    # delete语句
    def deLete(self, tablename, condition):
        sql = "delete from " + tablename + " where " + condition
        self.cur.execute(sql)

    # select语句
    def seLect(self, key, tablename, condition):
        sql = "select " + key + " from " + tablename + " where " + condition
        self.cur.execute(sql)
        print self.cur.fetchall()

    # 析构函数
    def __del__(self):
        print "成功析构"


if __name__ == '__main__':
    a = My2("root", "127.0.0.1", "redhat")
    a.connectDB()
