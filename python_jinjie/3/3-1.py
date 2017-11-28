# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
# 如何实现可迭代对象和迭代器对象
# 实际案例:
# 某软件要求:抓取天气城市信息:北京:17-22....,如果一次抓取s所有天气再显示,显示第一个城市气温时,有很高的延时,并且浪费空间,我们期望"用时访问"d的策略,并把s所有城市封装到y一个对象里,可用for语句迭代,怎么实现?
# def getWeather(city):
#     r = requests.get(u"http://wthrcdn.etouch.cn/weather_mini?city="+city)
#     data = json.loads(r.content)
#     data =  data['data']['forecast'][0]
#     return "%s:%s,%s"%(city,data['low'],data['high'])
# print  getWeather(u"北京")
# print  getWeather(u"长春")

import requests
import json
from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u"http://wthrcdn.etouch.cn/weather_mini?city=" + city)
        data = json.loads(r.content)
        data = data['data']['forecast'][0]
        return "%s:%s,%s" % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable([u"北京",u"河南",u"南京",u"上海"]):
    print x
