# -*- coding: utf-8 -*-
import json
import traceback

import requests
import re
import urllib2
import os
from bs4 import BeautifulSoup
import MySQLdb as mdb
import sys
import datetime
import time

reload(sys)
sys.setdefaultencoding('utf-8')


class Db():
    def __init__(self):
        self.db_host = "127.0.0.1"
        self.db_port = "3306"
        self.db_user = "root"
        self.db_pwd = ""
        self.db_name = "39eh.com"
        self.db_conn = None
        self.db_curr = None

    def check_conn(self):
        try:
            self.db_conn.ping()
        except:
            return False
        else:
            return True

    def conn(self):
        self.db_conn = mdb.connect(self.db_host, self.db_user, self.db_pwd, self.db_name, charset='utf8')
        self.db_conn.autocommit(False)
        self.db_curr = self.db_conn.cursor()

    def fetchone(self):
        return self.db_curr.fetchone()

    def fetchall(self):
        return self.db_curr.fetchall()

    def execute(self, sql, args=None, falg=False):
        if not self.db_conn:
            self.conn()
        try:
            if args:
                rs = self.db_curr.execute(sql, args)
            else:
                rs = self.db_curr.execute(sql)
            return rs
        except Exception, e:
            if self.check_conn():
                print "execute error"
                traceback.print_exc()
            else:
                print 'reconnect mysql'
                self.conn()
                if args:
                    rs = self.db_curr.execute(sql, args)
                else:
                    rs = self.db_curr.execute(sql)
                return rs

    def commit(self):
        self.db_conn.commit()

    def rollback(self):
        self.db_conn.rollback()

    def close(self):
        self.db_conn.close()
        self.db_curr.close()

    def last_row_id(self):
        return self.db_curr.lastrowid

class WenzhangSplide():
    def __init__(self):
         # 基础url
        self.base_url = u"http://www.39eh.com"
        self.db = Db()
    def gethtml(self, url):
        request = urllib2.Request(url)
        # request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
        response = urllib2.urlopen(request)
        htmlStr = response.read()
        soup = BeautifulSoup(htmlStr, "lxml")
        return soup



class EhcomSplide():
    def __init__(self):
        # 基础url
        self.base_url = u"http://www.39eh.com"
        self.db = Db()

    def gethtml(self, url):
        request = urllib2.Request(url)
        # request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
        response = urllib2.urlopen(request)
        htmlStr = response.read()
        soup = BeautifulSoup(htmlStr, "lxml")
        return soup

    def start_spider(self, url, type):
        soup = self.gethtml(url)
        box_list = soup.select(".list-pianyuan-box")
        cid = self.get_category(soup, type)
        self.get_list_con(box_list, cid)

    def get_category(self, soup, type):
        # 建立分类
        catgory_tite = soup.title.string
        try:
            self.db.execute("INSERT INTO category(`catgory`,`type`) VALUES(%s,%s)", (catgory_tite, type))
            cid = self.db.last_row_id()
        except:
            traceback.print_exc()
            self.db.rollback()
        else:
            self.db.commit()
        return cid

    def get_list_con(self, box_list, cid):
        # 获取列表详情
        for i in range(0, len(box_list)):
            time.sleep(3)
            restive_path = box_list[i].select(".list-pianyuan-box-l img")[0].attrs['src']
            dirname = os.path.dirname(restive_path)
            if os.path.isdir(u"test" + dirname) == False:
                os.makedirs(r"test" + dirname, 0755)
            src = self.base_url + restive_path
            self.pic_download(u"test" + box_list[i].select(".list-pianyuan-box-l img")[0].attrs['src'], src)

            dya1 = box_list[i].select(".dya1")
            title = dya1[0].select('a')[0].attrs['title']
            zhuyan = dya1[1].string
            diqu = dya1[2].string
            update_time = dya1[3].string
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            href = box_list[i].select("div[align=center] a")[0].attrs['href']
            # 进入详情页,获取playlist是几个播放源
            play_list_str = self.get_con_detail(href)
            source_dict = self.get_playlist_tags(play_list_str)
            bofang_url = source_dict['bofang_url']
            bt_url = source_dict['bt_url']
            print bt_url,bofang_url

            try:
                self.db.execute(
                        "INSERT INTO zaixianyingyuan (`cid`,`title`,`img`,`zhuyan`,`diqu`,`time`,`bofang_url`,`create_time`,`bt_url`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (cid, title, restive_path, zhuyan, diqu, update_time, bofang_url, create_time, bt_url))
            except:
                traceback.print_exc()
                self.db.rollback()
            else:
                self.db.commit()

    # 处理play_list
    def get_playlist_tags(self, play_list_str):
        source_dict = {
            "bofang_url": "",
            "bt_url": ""
        }
        if (len(play_list_str) == 2):
            source_dict = self.deal_with_two(play_list_str)
        else:
            bofang_url = self.deal_with_one(play_list_str)
            source_dict['bofang_url'] = bofang_url
            source_dict['bt_url'] = ""
        return source_dict

    # 进入详情页面
    def get_con_detail(self, href):
        detail_url = self.base_url + href
        soup = self.gethtml(detail_url)
        play_list = soup.select(".playlist")
        return play_list

    # 处理只有一个play_List
    def deal_with_one(self, play_list_str):
        play_list = play_list_str[0].select("li")

        true_play_urls = []
        for i in range(0, len(play_list)):
            play_href = self.base_url + play_list[i].select("a")[0].attrs["href"]
            try:
                play_html = urllib2.urlopen(play_href).read()
                preg = r'(\'Url\':)([\s\S]*)?(.rmvb|.mp4|.wmv|.avi|.3gp)'
                pattern = re.compile(preg)
                matcher = re.search(pattern, play_html)
                suffix = matcher.group(3)
                print play_href
                true_play_urls.append(matcher.group(2) + suffix)
            except:
                true_play_urls.append("")

        print true_play_urls
        return json.dumps(true_play_urls)

    # 处理有两个play_List的情况
    def deal_with_two(self, play_list_str):
        play_list = play_list_str[0].select("li")
        true_play_urls = []
        for i in range(0, len(play_list)):
            play_href = self.base_url + play_list[i].select("a")[0].attrs["href"]
            try:
                play_html = urllib2.urlopen(play_href).read()
                preg = r'(var url = \()([\s\S]*)?(.rmvb|.mp4|.wmv|.avi|.3gp)'
                pattern = re.compile(preg)
                matcher = re.search(pattern, play_html)
                suffix = matcher.group(3)
                true_play_urls.append(matcher.group(2).encode("utf-8") + suffix)
            except:
                true_play_urls.append("")
        # print true_play_urls
        # return json.dumps(true_play_urls)
        bt_url = play_list_str[1].select("li a")[0].attrs['href']
        source_dict = {
            'bofang_url': true_play_urls,
            'bt_url': bt_url
        }
        return source_dict

    # 暂时舍弃
    def get_con_detail1(self, href):
        detail_url = self.base_url + href
        soup = self.gethtml(detail_url)
        play_list = soup.select(".playlist li")
        true_play_urls = []
        for i in range(0, len(play_list)):
            play_href = self.base_url + play_list[i].select("a")[0].attrs["href"]
            try:
                play_html = urllib2.urlopen(play_href).read()
                preg = r'(\'Url\':)([\s\S]*)?(.rmvb)'
                pattern = re.compile(preg)
                matcher = re.search(pattern, play_html)
                print play_href
                true_play_urls.append(matcher.group(2) + ".rmvb")
            except:
                return true_play_urls.append("")

        print true_play_urls
        return json.dumps(true_play_urls)

    def pic_download(self, dir, src):
        res = requests.get(src)
        with open(dir, 'wb') as code:
            code.write(res.content)
            code.closed


if __name__ == '__main__':
    eh = EhcomSplide()
    #104.247.205.99
    for i in range(1, 5):
        print  "http://www.39eh.com/VOD10/list_" + str(i) + ".html"
        eh.start_spider("http://www.39eh.com/VOD10/list_" + str(i) + ".html", 1)
        time.sleep(5)
