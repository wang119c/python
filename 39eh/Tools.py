# -*- coding: utf-8 -*-
import urllib2
import time

from bs4 import BeautifulSoup


class Tools():
    def gethtml(self, url, reget=5):
        try:
            request = urllib2.Request(url)
            # request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
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
