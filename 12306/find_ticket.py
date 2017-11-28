import time
import datetime
import requests
import json


def fetch_data(t, start, end, fd):
    "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-04-22&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CDW&=ADULT"
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
    for data in datas['data']:
        out = u"-----------------------\n"
        out += data['queryLeftNewDTO']['from_station_name']
        out += u" " + data['queryLeftNewDTO']['start_station_name']
        out += u" " + data['queryLeftNewDTO']['end_station_name']
        out += u" " + data['queryLeftNewDTO']['to_station_name']
        out += u" " + data['queryLeftNewDTO']['start_time']
        out += u" " + data['queryLeftNewDTO']['arrive_time']
        out += u" " + data['queryLeftNewDTO']['wz_num']
        out += u" " + data['queryLeftNewDTO']['tz_num']
        s = out.encode('utf-8')
        fd.write(s)
        fd.write('\n')


if __name__ == '__main__':
    with open("find_ticket.txt", 'w') as fd:
        fetch_data((datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d"), 'BJP', 'CDW', fd)
