# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
import codecs
import json
from scrapy.exporters import JsonItemExporter
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


# 自定义写入json
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        spider.close()


# 插入数据库的一种方法
class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect("127.0.0.1", 'root', '', 'cms', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # insert_sql = "insert into `article`(`title`,`create_date`,`url`,`url_object_id`,`front_image_url`,`front_image_path`,`tags`,`content`) VALUE (%s,%s,%s,%s,%s,%s,%s,%s)"
        # self.cursor.execute(insert_sql, (
        #     item['title'], item['create_time'], item['url'], item['url_object_id'], item['front_image_url'],
        #     item['front_image_path'], item['tags'], item['content']))


        insert_sql = "insert into `article`(`title`,`create_date`,`url`,`url_object_id`,`front_image_path`,`tags`,`content`) VALUE (%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(insert_sql, (
            item['title'], item['create_time'], item['url'], item['url_object_id'], item['front_image_path'],
            item['tags'],
            item['content']))
        self.conn.commit()


# 异步插入数据库
class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
                host=settings['MYSQL_HOST'],
                user=settings['MYSQL_USER'],
                passwd=settings['MYSQL_PWD'],
                db=settings['MYSQL_DBNAME'],
                charset='utf8',
                cursorclass=MySQLdb.cursors.DictCursor,
                use_unicode=True
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用stwited将mysql变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)

    def handle_error(self, failure):
        print(failure)

    def do_insert(self, cursor, item):
        # insert_sql = "insert into `article`(`title`,`create_date`,`url`,`url_object_id`,`front_image_path`,`tags`,`content`,`front_image_url`,`zan`,`fav`,`comment`) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # cursor.execute(insert_sql, (
        #     item['title'], item['create_time'], item['url'], item['url_object_id'], item['front_image_path'],
        #     item['tags'],
        #     item['content'],item['front_image_url'][0],item['zan'],item['fav'],item['comment']))

        # 执行具体的插入
        # 根据不同的tem,构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)


# 调用scrapy 提供的导出json
class JsonExporterPipeline(object):
    def __init__(self):
        self.file = open("article.json", "wb")
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path
        return item
