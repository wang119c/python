# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何解析xml文档
from xml.etree.ElementTree import parse

f = open('test.xml')
et = parse(f)
root = et.getroot()

root.tag
root.attrib
root.text
