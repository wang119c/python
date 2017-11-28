# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
from ArticleSpider.items import JobBoleArticleItem
from ArticleSpider.utils.common import get_md5
import datetime
from scrapy.loader import ItemLoader


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        '''
        1.获取文章列表页中的文章url并交给scrapy 下载并进行解析
        2.获取下一页的url 并j交给scrapy进行下载,下载完成交给parse
        :param response:
        :return:
        '''
        # 解析列表页中所有文章的url并交给scrapy下载进行解析
        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            img_url = post_node.css('img::attr(src)').extract_first('')
            if 'http:' not in img_url:
                img_url = 'http:' + img_url
            post_url = post_node.css('::attr(href)').extract_first('')
            yield Request(url=parse.urljoin(response.url, post_url), meta={'front_image_url': img_url},
                          callback=self.parse_detail)
        # 提取下一页url 交给scrapy 下载
        next_url = response.css('.next.page-numbers::attr(href)').extract_first('')
        if next_url:

            tets = parse.urljoin(response.url, next_url)
            pass
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        article_item = JobBoleArticleItem()

        front_image_url = response.meta.get('front_image_url', '')  # 文章封面图
        # css 选择器
        title = response.css('.entry-header h1::text').extract_first('')
        create_time = response.css('p.entry-meta-hide-on-mobile::text').extract()[0].strip().replace(' ·', '')
        zan = int(response.css('.vote-post-up h10::text').extract()[0])
        fav_re = re.match(r'.*(\d+).*', response.css('.bookmark-btn::text').extract()[0])
        if fav_re:
            fav = int(fav_re.group(1))
        else:
            fav = 0
        comment_re = re.match(r'.*(\d+).*', response.css('a[href="#article-comment"] span::text').extract()[0])
        if comment_re:
            comment = int(comment_re.group(1))
        else:
            comment = 0
        content = response.css("div.entry").extract()[0]
        tag_list = response.css('p.entry-meta-hide-on-mobile a::text').extract()
        tag = [x for x in tag_list if not x.strip().endswith('评论')]
        tags = ','.join(tag)

        article_item['url_object_id'] = get_md5(response.url)
        article_item['title'] = title
        try:
            create_time = datetime.datetime.strptime(create_time, "%Y/%m/%d").date()
        except Exception as e:
            create_time = datetime.datetime.now()
        article_item['create_time'] = create_time
        article_item['url'] = response.url
        article_item['front_image_url'] = [front_image_url]
        article_item['zan'] = int(zan)
        article_item['fav'] = int(fav)
        article_item['comment'] = int(comment)
        article_item['tags'] = tags
        article_item['content'] = content


        # 通过itemloader加载item  另一种加载item方式
        # item_loader = ItemLoader(item=JobBoleArticleItem(),response=response)
        # item_loader.add_css('title','.entry-header h1::text')
        # item_loader.add_value('url',response.url)
        # item_loader.add_value('url_object_id',get_md5(response.url))
        # item_loader.add_css('create_time','p.entry-meta-hide-on-mobile::text')
        # item_loader.add_value('front_image_url',[front_image_url])
        # item_loader.add_css('zan','.vote-post-up h10::text')
        # item_loader.add_css('fav','.vote-post-up h10::text')
        # item_loader.add_css('zan','.bookmark-btn::text')
        # item_loader.add_css('comment','a[href="#article-comment"] span::text')
        # item_loader.add_css('tags','p.entry-meta-hide-on-mobile a::text')
        # item_loader.add_css('content',"div.entry")
        # article_item = item_loader.load_item()
        # item_loader.add_xpath()

        yield article_item
