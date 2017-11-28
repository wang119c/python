# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from project24.items import CommitItem


class StationSQLPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='train', charset='utf8')
        self.cursor = self.conn.cursor()
        self.sql = "insert into `stations`(`bureau`,`station`,`name`,`address`,`passenger`,`luggage`,`package`)  VALUES(%s,%s,%s,%s,%s,%s,%s)"

    def process_item(self, item, spider):
        if isinstance(item, CommitItem):
            self.conn.commit()
        else:
            self.cursor.execute(self.sql, (
                item['bureau'], item['station'], item['name'], item['address'], item['passenger'],
                item['luggage'], item['package']))
