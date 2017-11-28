# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from scrapy.exceptions import DropItem


# from tutorial.items import CommitItem

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class ProvincePipeline2(object):
    def process_item(self, item, spider):
        print item['name'], '-----'
        return item


class ProvincePipeline1(object):
    def process_item(self, item, spider):
        if item['name']:
            return item
        else:
            raise DropItem('None item')


class AgencySQLPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='train', charset='utf8')
