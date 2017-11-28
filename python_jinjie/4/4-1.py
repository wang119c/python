# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何才分多种分割符的字符串?
# 实际案例:我们把某个字符串分割符号拆分成不同的字段,该字符串包含不同的分割付,如:s = 'asd./.';
# 其中,/等都是分隔符怎么处理?


# 方法一
# def mySplit(s, ds):
#     res = [s]
#     for d in ds:
#         t = []
#         map(lambda x: t.extend(x.split(d)), res)
#         res = t
#     return [x for x in res if x]
#
#
# s = 'asdgjagsdjyw./qwe.?qej|kda\tadkajlds'
# print mySplit(s, './\t|?')
# 方法二
import re

s = 'asdgjagsdjyw./qwe.?qej|kda\tadkajlds'
print re.split(r'[./\t|?]+', s)
