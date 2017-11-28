# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.exceptions import DropItem
from project23.items import CommitItem


# class Project23Pipeline(object):
#     def process_item(self, item, spider):
#         return item
#
#
# class ProvincePipeline2(object):
#     def process_item(self, item, spider):
#         print item['name'], '-----'
#         return item
#
#
# class ProvincePipeline1(object):
#     def process_item(self, item, spider):
#         if item['name']:
#             return item
#         else:
#             raise DropItem('None item')


class AgencySQLPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='train', charset='utf8')
        self.cursor = self.conn.cursor()
        self.sql = "insert into `test`(`province`,`city`,`county`,`address`,`window`,`start`)  VALUES(%s,%s,%s,%s,%s,%s)"

    def process_item(self, item, spider):
        if isinstance(item, CommitItem):
            self.conn.commit()
        else:
            self.cursor.execute(self.sql, (
                item['province'], item['city'], item['county'], item['address'], item['window'],
                item['start']))
