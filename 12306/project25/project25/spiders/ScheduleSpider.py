# -*- coding: utf-8 -*-
import scrapy
import datetime
import urllib
from scrapy import Request
import json
from project25.items import BriefItem, CommitItem, InfoItem


class ScheduleSpider(scrapy.Spider):
    name = "ScheduleSpider"

    def start_requests(self):
        url = "https://kyfw.12306.cn/otn/queryTrainInfo/getTrainName?"
        t = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
        params = {'date': t}
        s_url = url + urllib.urlencode(params)
        self.logger.debug("start_url" + s_url)
        yield Request(s_url, callback=self.parse, meta={'t': t})

    def parse(self, response):
        datas = json.loads(response.body)
        url = "https://kyfw.12306.cn/otn/czxx/queryByTrainNo?"
        for data in datas['data']:
            item = BriefItem()
            briefs = data['station_train_code'].split('(')
            item['train_no'] = data['train_no']
            item['code'] = briefs[0]
            briefs = briefs[1].split("-")
            item["start"] = briefs[0]
            item["end"] = briefs[1][:-1]
            yield item
            # https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=24000000T70X&from_station_telecode=BXP&to_station_telecode=CDW&depart_date=2017-04-21
        params = u"train_no=" + data["train_no"] + u"&from_station_telecode=BXP&to_station_telecode=CDW&depart_date=" + \
                 response.meta['t']
        yield Request(url + params, callback=self.parse_train_schedule, meta={'train_no': data['train_no']})

    def parse_train_schedule(self, response):
        stations = json.loads(response.body)
        datas = stations['data']['data']
        size = len(datas)
        for i in range(0, size):
            data = datas[i]
            info = InfoItem()
            info['train_no'] = response.meta['train_no']
            info['no'] = int(data['station_no'])
            info['station'] = data['station_name']
            if info['no'] == 1:
                info['type'] = 0
            elif size == info['no']:
                info['type'] = 1
            else:
                info['type'] = 2
            if data['start_time'] != u'----':
                info['start_time'] = data['start_time'] + u":00"
            else:
                info['start_time'] = None
            if data['arrive_time'] != u'----':
                info['arrive_time'] = data['arrive_time'] + u":00"
            else:
                info['arrive_time'] = None
            if data['stopover_time'] != u'----':
                info['stopover_time'] = data['stopover_time'] + u":00"
            else:
                info['stopover_time'] = None
            yield info
        yield CommitItem()
