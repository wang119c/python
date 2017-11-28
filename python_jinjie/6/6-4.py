# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何构建xml
# from xml.etree.ElementTree import Element,ElementTree
# from xml.etree.ElementTree import tostring
# e = Element('Data')
# e.set("name","abc")
# e.text = '123'
# # print tostring(e)
# # 添子元素
# e2 = Element("Row")
# e2.text = '7.000'
# e.append(e2)
#
# # print tostring(e)
# et = ElementTree(e)
# et.write('test.xml')


import csv
from xml.etree.ElementTree import Element, ElementTree


def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader()
        header = reader.next()
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(header, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
    return ElementTree(root)


