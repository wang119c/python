# -*- coding: utf-8 -*-

from random import randint
import timeit

data = [randint(-10, 10) for _ in xrange(10)]
s = set(data)
print  {x for x in s if x % 3 == 0}

# def one():
#     filter(lambda x: x >= 0, data)
# print timeit.timeit(stmt=one)
# timeit.Timer( filter(lambda x: x >= 0, data) )
# data = {
#     x: randint(60, 100) for x in xrange(1, 21)
#     }
#
# print {k: v for k, v in data.iteritems() if v > 90}
