# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如何派生内置不可变类型并修改其实例化行为?
class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        super(IntTuple, self).__init__(iterable)
t = IntTuple([1, -1, 'abc', 3])
print t
