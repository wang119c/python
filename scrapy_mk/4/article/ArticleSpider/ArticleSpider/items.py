# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


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