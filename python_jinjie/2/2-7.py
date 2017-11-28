# -*- coding: utf-8 -*-
# 如何让字典保持有序?
# 实际案例:
# 某编程竞赛系统,对参赛编程题进行计时,选手完成题目后,把该选手解题时用记录到字典中,以便赛后按选手名查询成绩(答题时间越短,成绩越好),{"zhangsan":(1,23),'lisi':(2,99)}
# 比赛结束后,按排名顺序,打印选手成绩?
from collections import OrderedDict
from time import time
from random import randint

# d = {}
# d['jim'] = (1, 20)
# d['bob'] = (2, 22)
# d['lei'] = (3, 33)
# for i in d :
#     print i
# d = OrderedDict()
# d['jim'] = (1, 20)
# d['bob'] = (2, 22)
# d['lei'] = (3, 33)
# for i in d :
#     print i

players = list("abcdefgs")
start = time()
d = OrderedDict()
for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    d[p] = (i+1,end-start)
    print p,i+1,end-start
for k in d :
    print k,d[k]
