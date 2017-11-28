import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def fetch_data(fd):
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9002"
    try:
        s = requests.get(url, verify=False)
    except Exception, e:
        print "fail", url
        raise e
    station_str = s.content.encode('utf-8')
    stations = station_str.split(u'@')
    for i in range(0, len(stations)):
        station = stations[i].split(u"|")
        if(len(station) == 1):
            continue
        out = station[1] + u"|" + station[2]+u"\n"
        fd.write(out)
if __name__ == '__main__':
    with open("station_code.txt", 'w') as fd:
        fetch_data(fd)
        print "ok"
