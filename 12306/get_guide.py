# -*- coding:utf-8 -*-
import requests
import time
import json


def fetch_provinces():
    url = "https://kyfw.12306.cn/otn/userCommon/allProvince"
    try:
        headers = {
            'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
        s = requests.get(url, headers=headers, verify=False)
    except Exception, e:
        print "fetch proviness. " + url
        raise e
    j = json.loads(s.content)
    return j['data']


def fetch_data(url, province, fd):
    try:
        # https://kyfw.12306.cn/otn/queryAgencySellTicket/query?province=%E5%AE%89%E5%BE%BD&city=&county=
        s = requests.get(url, params={"province": province, "city": "", "county": ""}, verify=False)
    except Exception,e:
        print "request url fail:", url, province.encode('utf-8')
        raise e
    datas = json.loads(s.content)
    for data in datas['data']['datas']:
        out = u''
        out += data['belong_station']
        out += u' ' + data['province']
        out += u' ' + data['city']
        out += u' ' + data['county']
        out += u' ' + data['agency_name']
        out += u' ' + data['address']
        out += u' ' + data['phone_no']
        out += u' ' + data['windows_quantity']
        start = data['start_time_am']
        end = data['stop_time_am']
        out += u" " + start[:2] + u":" + start[:2] + u"-" + end[:2] + u":" + end[2:]
        s = out.encode("utf-8")
        fd.write(s)
        fd.write("\n")
        print s


if __name__ == '__main__':
    url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query"
    provs = fetch_provinces()
    with open("province.txt", "w") as fd:
        for prov in provs:
            fetch_data(url, prov['chineseName'], fd)
