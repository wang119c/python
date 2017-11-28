# -*- coding: utf-8 -*-
import traceback

import time

import datetime

from Db import Db;
from Tools import Tools;
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Tupian():
    def __init__(self):
        self.base_url = u"http://www.39eh.com"
        self.db = Db()

    def run_spider(self, url, type):
        tool = Tools()
        soup = tool.gethtml(url)
        cid = self.get_category(soup, type)

        box_list = soup.select(".zxlist ul")
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
        for i in range(0, len(box_list)):
            time.sleep(3)
            title = box_list[i].select("a")[0].string
            print title
            date = box_list[i].select("li.zxsyd")[0].string
            href = self.base_url + box_list[i].select("a")[0].attrs['href']
            content = self.get_detail(href)
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                self.db.execute(
                        "INSERT INTO tupian (`cid`,`title`,`date`,`content`,`create_time`) VALUES(%s,%s,%s,%s,%s)",
                        (cid, title, date, content, create_time))
            except:
                traceback.print_exc()
                self.db.rollback()
            else:
                self.db.commit()

    def get_detail(self, url):
        tool = Tools()
        soup = tool.gethtml(url)
        content = soup.select(".temp23")[0]
        return content


if __name__ == '__main__':
    tp = Tupian()
    for i in range(105,183):
        print "http://www.39eh.com/PIC01/list_" + str(i) + ".html"
        tp.run_spider("http://www.39eh.com/PIC01/list_" + str(i) + ".html", 3)
