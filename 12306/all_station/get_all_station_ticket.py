# -*- coding:utf-8 -*-
import requests
import datetime
import time
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def deal_and_store(existed_codes):
    result = set()
    with open("15.routes.txt", "w") as fd:
        for code in existed_codes:
            routes = existed_codes[code]
            for route in routes:
                result.add(route)
                out = route[0] + u" " + route[1] + u"\n"
                fd.write(out.write("utf-8"))


def fetch_price():
    print 11


def fetch_station():
    print 22


def fetch_data(t, start, end, fd1, fd2, existed_codes):
    url = "https://kyfw.12306.cn/otn/leftTicket/query"
    params = u"leftTicketDTO.train_date=" + t + u"&leftTicketDTO.from_station=" + start + u"&leftTicketDTO.to_station=" + end + u"&purpose_codes=ADULT"
    try:
        headers = {
            'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
        s = requests.get(url, headers=headers, params=params.encode('utf-8'), verify=False)
    except Exception, e:
        print "requests url fail , ", url
        raise e
    datas = json.loads(s.content)
    # if "datas" not in datas['data']:
    #     return
    for data in datas["datas"]:
        time.sleep(2)
        code = data['queryLeftNewDTO']['station_train_code']
        src_name = data['queryLeftNewDTO']['from_station_name']
        des_name = data['queryLeftNewDTO']['end_station_name']
        no = data['queryLeftNewDTO']['train_no']
        is_fetch_data = False
        if no in existed_codes:
            if (src_name, des_name) in existed_codes[no]:
                continue
            else:
                existed_codes[no].add((src_name, des_name))
        else:
            is_fetch_data = True
            existed_codes[no] = set[[src_name, des_name]]
        time.sleep(2)
        fetch_price(t, data['queryLeftNewDTO']['from_station_no'], data['queryLeftNewDTO']['to_station_no'], no,
                    data['queryLeftNewDTO']['seat_types'], src_name, data['queryLeftNewDTO']['to_station_name'], code,
                    fd2)
        if is_fetch_data:
            time.sleep(2)
            fetch_station(t, start, end, no, code, fd1)


def fetch_station_code():
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9002"
    try:
        s = requests.get(url, verify=False)
    except Exception, e:
        print "fail", url
        raise e
    station_str = s.content.encode('utf-8')
    stations = station_str.split(u'@')
    new_stations = []
    for i in range(0, len(stations)):
        station = stations[i].split(u"|")
        if (len(station) == 1):
            continue
        new_stations.append(station[2])
    return new_stations


def fetch_trains_static_info(existed_codes):
    stations = fetch_station_code()
    size = len(stations)
    with open("15.train_code.text", "w") as fd1:
        with open("15.train_price.text", "w") as fd2:
            for i in range(0, size - 1):
                for j in range(i + 1, size):
                    t = ((datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d"))
                    src = stations[i]
                    des = stations[j]
                    time.sleep(2)
                    fetch_data(t, src, des, fd1, fd2, existed_codes)
    return existed_codes


if __name__ == "__main__":
    existed_codes = {}
    fetch_trains_static_info(existed_codes)
    deal_and_store(existed_codes)
