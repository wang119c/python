# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["resource-zone.com"]
    start_urls = ['https://www.resource-zone.com/forum/f/chinese.32/']

    # def parse(self, response):

