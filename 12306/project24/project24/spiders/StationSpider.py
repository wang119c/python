# -*- coding: utf-8 -*-
import os

import scrapy
import json
import urllib
from scrapy.http.request import Request
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from project24.items import CommitItem, StationsItem


class StationSpider(scrapy.Spider):
    name = "StationSpider"
    start_urls = [
        "http://www.12306.cn/mormhweb/kyyyz/"
    ]
    def start_requests(self,response):
        pass
    def parse(self, response):
        names = response.css("#secTable > tbody > tr > td::text").extract()
        sub_urls = response.css('#mainTable  td.submenu_bg > a::attr(href)').extract()
        for i in range(0, len(names)):
            sub_url1 = response.url + sub_urls[i * 2][2:]
            yield Request(sub_url1, callback=self.parse_station, meta={'bureau': names[i], 'station': True})

            sub_url2 = response.url + sub_urls[i * 2 + 1][2:]
            yield Request(sub_url2, callback=self.parse_station, meta={'bureau': names[i], 'station': False})

    def parse_station(self, response):
        datas = response.css('table table tr')
        self.logger.debug(datas)
        if len(datas) < 2:
            self.logger.info("no item")
            return
        for i in range(0, len(datas)):
            if i < 2:
                continue
            infos = datas[i].css('td::text').extract()
            item = StationsItem()
            item['bureau'] = response.meta['bureau']
            item['station'] = 1 if response.meta['station'] else 0
            item['name'] = infos[0]
            item['address'] = infos[1]
            item['passenger'] = infos[2].strip()
            item['passenger'] = 1 if infos[2].strip() != u"" else 0
            item['luggage'] = 1 if infos[3].strip() != u"" else 0
            item['package'] = 1 if infos[4].strip() != u"" else 0
            yield item
        yield CommitItem()
