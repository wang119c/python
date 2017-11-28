# -*- coding: utf-8 -*-
import scrapy
import re
import json


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']
    headers = {
        'Host': 'www.zhihu.com',
        'Referer': 'https://www.zhihu.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36 QQBrowser/3.7.3773.400'
    }

    def parse(self, response):
        pass

    def start_requests(self):
        return [scrapy.Request("https://www.zhihu.com/#signin", headers=self.headers, callback=self.login)]

    def login(self, response):
        response_text = response.text
        match_obj = re.match('.*name="_xsrf" value="(.*?)"', response_text, re.DOTALL)
        xsrf = ''
        if match_obj:
            xsrf = match_obj.group(1)

        return [scrapy.FormRequest(
                url='https://www.zhihu.com/login/phone_num',
                formdata={
                    '_xsrf': xsrf,
                    'password': 'wanghui1203',
                    'phone_num': '13126858018'
                },
                headers=self.headers,
                callback=self.check_login
        )]

    def check_login(self, response):
        # 验证服务器是否登录
        text_json = json.loads(response.text)
        if 'msg' in text_json and text_json['msg'] == '登录成功':
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers)
