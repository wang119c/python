# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
# 如何多个小字符串拼接成一个大字符串
# s1 = '123124235'
# s2 = 'asdasda'
# print s1+s2
# 方法一
# pl = ['12','asd','3d','de','12d']
# s = ''
# for x in pl:
#     s += x
# print s
# 方法二
# print ';'.join(['12','asd','3d','de','12d'])
# print ''.join(['12','asd','3d','de','12d'])
# pl = ['12','asd','3d','de','12d']
# print ''.join(pl)

pl = ['abc',123,45,'xyz']
print ''.join(str(x) for x in pl)