# -*- coding: utf-8 -*-
import scrapy
import json
from tutorial.items import ProvinceItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["12306.cn"]
    start_urls = [
        "https://kyfw.12306.cn/otn/userCommon/allProvince"
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.ProvincePipeline1': 300,
            'tutorial.ProvincePipeline2': 400,
        }
    }

    def parse(self, response):
        j = json.loads(response.body)
        for prov in j['data']:
            item = ProvinceItem()
            item['name'] = prov['chineseName']
            yield item
        item = ProvinceItem()
        item["name"] = None
        yield item
