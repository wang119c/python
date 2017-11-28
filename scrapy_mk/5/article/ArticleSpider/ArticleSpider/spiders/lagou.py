# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from items import LagousJobItem, LagousJobItemLoder
from utils.common import get_md5
from datetime import datetime


# 第六课件
class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'), follow=True),
        Rule(LinkExtractor(allow=r'gongsi/j\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )

    def parse_job(self, response):
        item_loader = LagousJobItemLoder(item=LagousJobItem(), response=response)
        item_loader.add_css('title', '.job-name::attr(title)')
        item_loader.add_value('url', response.url)
        item_loader.add_value('url_object_id', get_md5(response.url))
        item_loader.add_css('salary', '.job_request .salary::text')
        item_loader.add_css('job_city', '.job_request span:nth-of-type(2)::text')
        item_loader.add_css('work_year', '.job_request span:nth-of-type(3)::text')
        item_loader.add_css('degree_need', '.job_request span:nth-of-type(4)::text')
        item_loader.add_css('job_type', '.job_request span:nth-of-type(5)::text')
        item_loader.add_css('pulish_time', '.publish_time::text')
        item_loader.add_css('tags', '.position-label .labels::text')
        item_loader.add_css('job_advantage', '.job-advantage p::text')
        item_loader.add_css('job_desc', '.job_bt div')
        item_loader.add_css('job_addr', '.work_addr')
        item_loader.add_css('company_name', '#job_company dt a img::attr(alt)')
        item_loader.add_css('company_url', '#job_company dt a::attr(href)')
        item_loader.add_value('crawl_time', datetime.now())
        job_item = item_loader.load_item()
        return job_item
