# -*- coding:utf-8 -*-
import time
import requests
import datetime
import json
import pymysql


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
        s = requests.get(url, params={"province": province, "city": "", "county": ""}, verify=False)
    except Exception, e:
        print "request url fail:", url, province.encode('utf-8')
        raise e
    datas = json.loads(s.content)
    for data in datas['data']['datas']:
        print data
        cursor.execute(
                "insert into test(province,city,county,address,window,start)  VALUES(%s,%s,%s,%s,%s,%s)",(data['province'],data['city'],data['county'],data['address'],data['windows_quantity'],data['start_time_am']))
if __name__ == "__main__":
    url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query"
    provs = fetch_provinces()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='train', charset='utf8')
    cursor = conn.cursor()
    for prov in provs:
        fetch_data(url, prov['chineseName'], cursor)
    conn.commit()
    cursor.close()
    conn.close()
