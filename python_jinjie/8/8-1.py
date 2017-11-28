# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何使用多线程?
# def handle():
#     # 处理逻辑
#     pass


# 方法一:
# from threading import Thread
# t = Thread(target=handle,args=(1,))
# t.start()
# 方法二:
# from threading import Thread
#
#
# class MyThread(Thread):
#     def __init__(self, sid):
#         Thread.__init__(self)
#         self.sid = sid
#
#     def run(self):
#         handle(self.sid)

# 如何实现线程之间的通信
import requests
from StringIO import StringIO
# from xml_pretty
from threading import Thread


class DownloadThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid
        self.url = ""
        # self.url =

    def download(self, url):
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        data = self.download(self.url)


class CovertThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def csvToXml(self, scsv, fxml):
        pass

    def run(self):
        pass
