# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何读写文本文件?
# 文件如:(utf-8,gbk,big5)
s = "你好"
# print s.encode('gbk').decode('gbk')
# print s.encode('utf-8')


f = open('py2.txt','w')
s = u'你好'
f.write(s.encode('utf-8'))
f.close()

f = open('py2.txt','r')
t = f.read().decode('utf-8')
print t