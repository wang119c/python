# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如何进行反向迭代及r如何s实现反向迭代?
# 实际案例:
# 实现一个连续浮点数的连续发生器,根据给定范围c产生:一些浮点数,正向3.0<3.2.....反向:4.5>4.0
# l = [1,2,3,4,5]
# for x in reversed(l):
#     print x
# class FloatRange:
#     def __init__(self, start, end, step=0.1):
#         self.start = start
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         t = self.start
#         while t <= self.end:
#             yield t
#             t += self.step
#
#     def __reversed__(self):
#         t = self.end
#         while t >= self.start:
#             yield t
#             t -= self.step
# for x in FloatRange(1.0,4.0,0.5):
#     print x

# for x in reversed(FloatRange(1.0,4.0,0.5)):
#     print x

# 如何对迭代器做切片操作?
# 实际案例:有某个文本文件,我们去其中某范围的内容,如100-300 行之间的内容,python 中的文件,是可迭代的对象,我们是否可以使用类似列表切片的方法得到一个00-300h行的内容生成器呢
from itertools import islice

f  = open('word.txt','r')
islice(f,10,20)
for x in islice(f,10,20):
    print x