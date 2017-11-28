# -*- coding: utf-8 -*-
# author huizi
# email 1052430943@qq.com
import os
import urllib2
import time

from bs4 import BeautifulSoup
from selenium import webdriver


class Tools:
    def usePhantomjsGetHtml(self, url, reget=5):
        try:
            path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/bin/phantomjs"
            driver = webdriver.PhantomJS(
                    executable_path=path
            )
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            return soup
        except:
            if reget >= 1:
                # 如果getHtml失败，则再次尝试5次
                print 'getHtml error,reget...%d' % (6 - reget)
                time.sleep(2)
                return self.usePhantomjsGetHtml(url, reget - 1)
            else:
                print 'request url:' + url
                print 'failed to fetch html'
                exit()

    def gethtml(self, url, reget=5):
        try:
            request = urllib2.Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
            response = urllib2.urlopen(request)

            htmlStr = response.read()
            soup = BeautifulSoup(htmlStr, "lxml")
            return soup
        except:
            if reget >= 1:
                # 如果getHtml失败，则再次尝试5次
                print 'getHtml error,reget...%d' % (6 - reget)
                time.sleep(2)
                return self.gethtml(url, reget - 1)
            else:
                print 'request url:' + url
                print 'failed to fetch html'
                exit()

    def get_no_soup(self, url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        htmlStr = response.read()
        return htmlStr;
