# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何对字符串进行左右,居中对齐
# 方法一
# s = 'abc'
# print  s.ljust(20)
# print  s.rjust(20)
# print  s.center(20)
# 方法二
# s = 'abc'
# print format(s, '<20')
# print format(s, '>20')
# print format(s, '^20')

d = {
    'zhangsan': 10,
    'lisi': 10,
    'wangd': 20
}
w = max(map(len, d.keys()))
s = '{'
for k in d:
    s += format(k, '<' + str(w)) + ":" + str(d[k])+'\n'
s += '}'
print s