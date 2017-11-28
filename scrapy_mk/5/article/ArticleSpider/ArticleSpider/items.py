# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_time = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    zan = scrapy.Field()
    fav = scrapy.Field()
    comment = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()


# 用loader的方法去做的item
# def add_jobbole(value):
#     return value+"-jobbloe"
# class LoaderJobBoleArticleItem(scrapy.Item):
#     title = scrapy.Field(
#         input_processor = MapCompose(add_jobbole)
#     )
#     create_time = scrapy.Field()
#     url = scrapy.Field()
#     url_object_id = scrapy.Field()
#     front_image_url = scrapy.Field()
#     front_image_path = scrapy.Field()
#     zan = scrapy.Field()
#     fav = scrapy.Field()
#     comment = scrapy.Field()
#     tags = scrapy.Field()
#     content = scrapy.Field()



# 拉钩
from w3lib.html import remove_tags
from datetime import time


def remove_splash(value):
    # 去掉工作的斜线
    return value.replace('/', '')


def handle_jobaddr(value):
    addr_list = value.split('\n')
    addr_list = [item.strip() for item in addr_list if item.strip() != '查看地图']
    return "-".join(addr_list)


class LagousJobItemLoder(ItemLoader):
    default_output_processor = TakeFirst()


class LagousJobItem(scrapy.Item):
    # 拉勾网职位
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field(
            input_processor=MapCompose(remove_splash),
    )
    work_year = scrapy.Field(
            input_processor=MapCompose(remove_splash),
    )
    degree_need = scrapy.Field(
            input_processor=MapCompose(remove_splash),
    )
    job_type = scrapy.Field()
    pulish_time = scrapy.Field()
    tags = scrapy.Field(
            input_processor=Join(',')
    )
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field()
    job_addr = scrapy.Field(
            input_processor=MapCompose(remove_tags, handle_jobaddr),
    )
    company_url = scrapy.Field()
    company_name = scrapy.Field()
    crawl_time = scrapy.Field()
    crawl_update_time = scrapy.Field()

    # 写入数据库
    def get_insert_sql(self):
        insert_sql = """
            insert into lagou(title,url,url_object_id,salary,job_city,work_year,degree_need,job_type,pulish_time,tags,job_advantage,job_desc,job_addr,company_url,company_name,crawl_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE salary = VALUES(salary)

        """
        param = (
            self['title'], self['url'], self['url_object_id'], self['salary'], self['job_city'], self['work_year'],
            self['degree_need'], self['job_type'], self['pulish_time'], self['tags'], self['job_advantage'],
            self['job_desc'], self['job_addr'], self['company_url'], self['company_name'], self['crawl_time'],
        )
        return insert_sql, param
