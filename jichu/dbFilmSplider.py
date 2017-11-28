#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author huizi
# email 1052430943@qq.com
import re
import pymongo
from config import config
from libs.Tools import Tools
import sys
import hashlib
import time

reload(sys)
sys.setdefaultencoding('utf-8')


class DbFilmSplider:
    def __init__(self, film_cate):
        self.film_cate = film_cate
        # 创建连接
        client = pymongo.MongoClient(config.HOST, config.PORT)
        db = client[config.DATABASE]
        self.moive_cols = db['movie']
        pass

    def start_spider(self, list_url):
        self.get_list(list_url)
        pass

    def get_list(self, list_url):
        soup = Tools().usePhantomjsGetHtml(list_url)
        box_list = soup.select(".table-striped.shadow-frame tr td")
        for td in box_list:
            title = td.select("a:nth-of-type(2)>span")[0].get_text(strip=True)  # 标题
            try:
                douban_score = td.select(".list-douban")[0].get_text(strip=True) or 0  # 评分
            except Exception as e:
                douban_score = 0
                print e
            old_updatetime = td.select(".text-info.f-right")[0].get_text(strip=True)  # 时间
            source = td.select("a:nth-of-type(2)>span")[0].get("href")  # 资源页面

            # 创建md5对象
            m = hashlib.md5()
            m.update(source)
            encryption_url = m.hexdigest()  # 加密资源页面
            film_cate = self.film_cate  # 整体分类 如 2.电视剧 和 1.电影

            # 先检查下
            old_data = self.moive_cols.find_one({'encryption_url': encryption_url})
            if old_data == None:
                detail_res = self.get_detail(source)
                if detail_res == False:
                    print "版权要求"
                    continue
                new_data = {
                    'title': title,
                    'hot_num':0,
                    'source': source,
                    'douban_score': douban_score,
                    'old_updatetime': old_updatetime,
                    'encryption_url': encryption_url,
                    'film_cate': film_cate,
                    'thumb_img': detail_res['thumb_img'],
                    'plot_introduce': detail_res['plot_introduce'],
                    'content_info': detail_res['content_info'],
                    'tags': detail_res['tags'],
                    'link_down_source': detail_res['link_down_source'],
                    'create_time': time.strftime('%Y-%m-%d', time.localtime(time.time()))
                }
                # 组合成mongodb所需要的数据
                self.moive_cols.save(new_data)
            else:
                pass

            print source + "抓取ok"

    def get_detail(self, source_url):
        print "开始抓取" + source_url
        soup = Tools().usePhantomjsGetHtml(source_url)
        shadow_frame = soup.select("div.shadow-frame")[0]
        row_fluid = shadow_frame.select('.row-fluid')
        # 缩略图
        try:
            thumb_img = row_fluid[1].select("#wx_pic img:nth-of-type(1)")[0].get('src')
        except Exception as e:
            print str(e) + "缩略图没有获取到"
            thumb_img = ""
        # 电影介绍
        try:
            plot_introduce = str(row_fluid[1].select(".span7")[0]).split('<br/>')
            new_plot_introduce = []
            for text in plot_introduce:
                re_h = re.compile('</?\w+[^>]*>')
                s = re_h.sub('', text)
                new_plot_introduce.append(s)
            plot_introduce = '<br/>'.join(new_plot_introduce)
        except Exception as e:
            print str(e) + '没有电影简介'
            plot_introduce = ""

        # 剧情简介
        try:
            content_info = row_fluid[2].get_text(' ', strip=True)
        except Exception as e:
            print "没有简介内容"
            content_info = ""
        # 标签
        try:
            tags = row_fluid[3].select(".badge.badge-warning i")
            tags_arr = []
            for tag in tags:
                tags_arr.append(tag.get_text(strip=True))
            tags = '|'.join(tags_arr)
        except Exception as e:
            print "标签为空"
            tags = ""
        # 种子下载地址
        try:
            seeds_tr = soup.select("#bs-docs-download tr")
        except Exception as e:
            print e
            return False

        link_down_source = []
        for seed_tr in seeds_tr:
            seed_a_href = seed_tr.select(".bd-address a")[0].get('href')
            seed_a_title = seed_tr.select(".bd-address a")[0].get_text(strip=True)
            seeds = seed_tr.select("td:nth-of-type(2) a")
            if len(seeds) != 0:
                seeds_arr = []
                for seed in seeds:
                    link_url = seed.get('href')
                    socure_name = seed.get_text(strip=True)
                    if socure_name == "迅雷":
                        source_type = 'xunlei'
                    elif socure_name == '旋风':
                        source_type = 'xuanfeng'
                    elif socure_name == '小米':
                        source_type = 'xiaomi'
                    elif socure_name == '看看':
                        source_type = 'kankan'
                    down_socurce = {}
                    down_socurce['link_url'] = link_url
                    down_socurce['source_type'] = source_type
                    seeds_arr.append(down_socurce)
                link_down_source.append({
                    'title': seed_a_title,
                    'link_url': seed_a_href,
                    'seeds': seeds_arr
                })
            else:
                # 百度云盘
                try:
                    passwd = seed_tr.select(".bd-address span")[0].get_text(strip=True)
                    link_down_source.append({
                        'title': seed_a_title,
                        'link_url': seed_a_href,
                        'passwd': passwd
                    })
                except Exception as es:
                    print es
        # seeds_title = seeds_tr.select("td.bd-address a")[0].get_text(strip=True)
        # seeds = seeds_tr.select("td:nth-of-type(2) a")
        # link_down_source = []
        # for seed in seeds:
        #     link_url = seed.get('href')
        #     socure_name = seed.get_text(strip=True)
        #     if socure_name == "迅雷":
        #         source_type = 'xunlei'
        #     elif socure_name == '旋风':
        #         source_type = 'xuanfeng'
        #     elif socure_name == '小米':
        #         source_type = 'xiaomi'
        #     elif socure_name == '看看':
        #         source_type = 'kankan'
        #     down_socurce = {}
        #     down_socurce['title'] = seeds_title
        #     down_socurce['link_url'] = link_url
        #     down_socurce['source_type'] = source_type
        #     link_down_source.append(down_socurce)
        # 百度云盘下载地址

        detail_arr = {
            'thumb_img': thumb_img,
            'plot_introduce': plot_introduce,
            'content_info': content_info,
            'tags': tags,
            'link_down_source': link_down_source
        }
        return detail_arr


if __name__ == '__main__':

    # 最新电影爬取
    db_film = DbFilmSplider(1)
    # 获取初始的页数
    soup = Tools().usePhantomjsGetHtml("http://www.bd-film.com/zx/index.htm")
    page_nums = soup.select(".input-prepend.input-append option")
    nums_arr = []
    for page_num in page_nums:
        num = page_num.get('value')
        nums_arr.append(int(num))

    start_page = 1
    last_page = max(nums_arr)

    date_time = time.strftime("%Y-%m-%d", time.localtime())

    try:
        with open('./tmp/' + date_time + '.txt', 'r') as f:
            s = f.read()
            start_page = s or start_page
            f.close()
    except Exception as e:
        with open('./tmp/' + date_time + '.txt', 'w') as f:
            f.write('' + str(start_page))
            f.close()

    start_page = int(start_page)
    while start_page <= last_page:
        url = "http://www.bd-film.com/zx/index_%s.htm" % start_page
        print url
        with open('./tmp/' + date_time + '.txt', 'w') as f:
            f.write('' + str(start_page))
            f.close()
        db_film.get_list(url)
        start_page = start_page + 1



        # for i in range(last_page):
        #     url = "http://www.bd-film.com/zx/index_%s.htm" % (i + 1)
        #     print url
        #     time.sleep(2)
        #     db_film.get_list(url)
