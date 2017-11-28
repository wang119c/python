# -*- coding:utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def fetch_data(url, bureau, desc, fd):
    try:
        s = requests.get(url)
    except Exception, e:
        print "request url fail"
        return
    b = BeautifulSoup(s.content, "html")
    datas = b.select("table table tr")
    if len(datas) <= 2:
        s = "find nothing " + url + " " + bureau.encode("utf-8") + " " + desc.encode("utf-8")
        fd.write(s + '\n')

    # 迭代获取的行
    for i in range(0, len(datas)):
        if i < 2:
            continue
        infos = datas[i].find_all('td')
        out = u''
        for info in infos:
            out += info.text
            out += u', '
        out += bureau + u', ' + desc
        s = out.encode("utf-8")
        fd.write(s)
        fd.write("\n")
        # print s


if __name__ == "__main__":
    url = "http://www.12306.cn/mormhweb/kyyyz/"
    try:
        s = requests.get(url)
    except Exception, e:
        print "requests url fail"
        raise e
    soup = BeautifulSoup(s.content, 'html')
    results = soup.select("#secTable > tbody > tr > td");
    sub_urls = soup.select("#mainTable td.submenu_bg > a")
    with open("9.final.txt", "w") as fd:
        for i in range(0, len(results)):
            sub_url1 = url + sub_urls[i * 2]["href"][2:]
            print sub_url1
            fetch_data(sub_url1, results[i].text, u"车站", fd)
            time.sleep(5)

            sub_url2 = url + sub_urls[i * 2 + 1]["href"][2:]
            print sub_url2
            fetch_data(sub_url2, results[i].text, u"乘务所", fd)
            time.sleep(5)
