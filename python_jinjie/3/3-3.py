# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如何使用生成器h函数实现可迭代对象?
# 实际案例:实现一个可迭代对象的类,它能迭代出给定范围的n内所有的素数:
# pn = PrintNumbers(1,)
# for k in pn :
#     print  k
# 输出结果;
# 2 3 4 5 ....

# def f():
#     print "in f(),1"
#     yield 1
#     print "in f(),2"
#     yield 2
#     print "in f(),3"
#     yield 3
# g = f()
# for x in g :
#     x


class PrimeNumbers():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNumber(self, k):
        if k < 2:
            return False
        for i in xrange(2, k):
            if (k % 2 == 0):
                return False
            return True

    def __iter__(self):
        for k in xrange(self.start, self.end+1):
            if self.isPrimeNumber(k):
                yield k

for x in PrimeNumbers(1,1000000000000000000):
    print  x