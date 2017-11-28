# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
# 如何在y一个for语句中迭代多个k可迭代的对象
# 实际案例:
# 1.某班学生期末考试成绩,语文,数学,英语分别存储在3个表中,同时迭代s三个列表,计算每个学生的总分
# from random import randint
#
# chinese = [randint(1, 100) for _ in xrange(40)]
# math = [randint(1, 100) for _ in xrange(40)]
# english = [randint(1, 100) for _ in xrange(40)]
#
# total = []
# for c, m, e in zip(chinese, math, english):
#     total.append(c + m + e)
# print total
# 2.某年级有4个班,某次考试每班英语成绩分别存储在4个列表中,依次迭代每个列表,统计全年成绩高于90分的人数(串行)
from random import randint
from itertools import chain
c1 = [randint(1, 100) for _ in xrange(40)]
c2 = [randint(1, 100) for _ in xrange(40)]
c3 = [randint(1, 100) for _ in xrange(40)]
c4 = [randint(1, 100) for _ in xrange(40)]
all_hight = []
for x in  chain(c1,c2,c3,c4):
    if (x < 90):
        continue;
    all_hight.append(x)
print all_hight
