# -*- coding: utf-8 -*-
import scrapy


class CoartSpider(scrapy.Spider):
    name = "coart"
    allowed_domains = ["coart.cn"]
    start_urls = ['http://coart.cn/']

    def parse(self, response):
        pass
