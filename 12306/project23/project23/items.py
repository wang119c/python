# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project23Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProvinceItem(scrapy.Item):
    name = scrapy.Field()


class AgencyItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    county = scrapy.Field()
    address = scrapy.Field()
    window = scrapy.Field()
    start = scrapy.Field()


class CommitItem(scrapy.Item):
    pass
