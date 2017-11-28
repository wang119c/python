# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class DailiIpsSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/']

    def start_requests(self):
        res = []
        for i in range(1, 2):
            url = 'http://www.xicidaili.com/nn/%d' % i
            req = scrapy.Request(url)
            res.append(req)
        return res

    def parse(self, response):
        table = response.xpath('//table[@id="ip_list"]')[0]
        print response
