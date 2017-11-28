# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CommitItem(scrapy.Item):
    pass


class StationItem(scrapy.Item):
    pass


class ProvinceItem(scrapy.Item):
    name = scrapy.Field()


class AgencyItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    county = scrapy.Field()
    address = scrapy.Field()
    widows = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()
