import scrapy

from tutorial.items import TutorialItem


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['coart.cn']
    start_urls = [
        'http://www.coart.cn'
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2] + ".txt"

        item = TutorialItem()
        item['title'] = response.xpath("/html/body/div[8]/div[2]/div").extract()
        yield item
    # for li in lis:
    #     title = li.xpath('a/text()').extract()
    #     link = li.xpath('a/@href').extract()
    #     desc = li.xpath('text()').extract()
    #     print(title)


    # item = TutorialItem()
    # item['title'] = li.xpath('/a/p[2]/text()').extract()
    # item['link'] = li.xpath('a/@href').extract()
    # item['desc'] = li.xpath('p[@class="ilsh_tese"]/span/text()').extract()
    # yield item
    # print(item['title'],item['link'],item['desc'])
    # with open(filename,'wb') as f:
    #     f.write(item['link'])
    #     f.write(item['title'])
    #     f.write(item['desc'])
