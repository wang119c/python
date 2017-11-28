# -*- coding: utf-8 -*-
import traceback
import MySQLdb as mdb

class Db():
    def __init__(self):
        self.db_host = "127.0.0.1"
        self.db_port = "3306"
        self.db_user = "root"
        self.db_pwd = ""
        self.db_name = "39eh.com"
        self.db_conn = None
        self.db_curr = None

    def check_conn(self):
        try:
            self.db_conn.ping()
        except:
            return False
        else:
            return True

    def conn(self):
        self.db_conn = mdb.connect(self.db_host, self.db_user, self.db_pwd, self.db_name, charset='utf8')
        self.db_conn.autocommit(False)
        self.db_curr = self.db_conn.cursor()

    def fetchone(self):
        return self.db_curr.fetchone()

    def fetchall(self):
        return self.db_curr.fetchall()

    def execute(self, sql, args=None, falg=False):
        if not self.db_conn:
            self.conn()
        try:
            if args:
                rs = self.db_curr.execute(sql, args)
            else:
                rs = self.db_curr.execute(sql)
            return rs
        except Exception, e:
            if self.check_conn():
                print "execute error"
                traceback.print_exc()
            else:
                print 'reconnect mysql'
                self.conn()
                if args:
                    rs = self.db_curr.execute(sql, args)
                else:
                    rs = self.db_curr.execute(sql)
                return rs

    def commit(self):
        self.db_conn.commit()

    def rollback(self):
        self.db_conn.rollback()

    def close(self):
        self.db_conn.close()
        self.db_curr.close()

    def last_row_id(self):
        return self.db_curr.lastrowid