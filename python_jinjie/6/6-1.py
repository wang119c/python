# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何读写csv数据?
# 实际案例:可以通过公开的api获取数据集 http://table.finance.yahoo.com/table.csv?s= 0000001.sz
# 请将这样数据集合保存在另一个csv中

from urllib import urlretrieve
import csv

with open('pingan.csv','rd') as rf :
    reader = csv.reader(rf)
    with open('pingan_cope.csv','wd') as wf :
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerrow(headers)
        for row in reader:
            if row[0] < "2016-01-01":
                break
            writer.writerrow(row)






# urlretrieve('http://table.finance.yahoo.com/table.csv?s= 0000001.sz','pingan.csv')
# import csv
# rf = open('pingan.csv','rb')
# reader = csv.read(rf)
# reader.next()
# wf = open('pingan_cope.csv','wb')
# writer = csv.writer(wf)
# writer.writerrow(reader.next())
# wf.flush()
#
#
#
# print reader

