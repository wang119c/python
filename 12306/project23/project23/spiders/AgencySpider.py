# -*- coding: utf-8 -*-
import scrapy
import json
import urllib
from scrapy.http.request import Request
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from project23.items import CommitItem, ProvinceItem, AgencyItem


class AgenySpider(scrapy.Spider):
    name = "AgenySpider"
    # allowed_domains = ["12306.cn"]
    start_urls = [
        "https://kyfw.12306.cn/otn/userCommon/allProvince"
    ]

    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'project23.AgencySQLPipeline': 300
    #     }
    # }

    def parse(self, response):
        province = json.loads(response.body.decode())
        url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query?"
        for prov in province['data']:
            params = {"province": prov['chineseName'].encode("utf-8"), "city": "", "county": ""}
            s_url = url + urllib.urlencode(params)
            yield Request(s_url, callback=self.parse_agecy)

    def parse_agecy(self, response):
        datas = json.loads(response.body.decode())
        for data in datas['data']['datas']:
            item = AgencyItem()
            item['province'] = data['province']
            item['city'] = data['city']
            item['county'] = data['county']
            item['address'] = data['address']
            item['window'] = data['windows_quantity']
            item['start'] = data['start_time_am']
            yield item
        yield CommitItem()
