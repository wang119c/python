# -*- coding: utf-8 -*-
# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3
# 可以写成
# 提高元素可读性 方案一
# NAME,AGE,SEX,EMAIL = xrange(4)
# student = ("zhangsan",18,"man","1056@qq.com")
# print student[NAME]
# print student[AGE]
# print student[SEX]
# print student[EMAIL]
# 提高元素可读性 方案二
# from collections import namedtuple
# Student = namedtuple("Student",['name','age','sex','email'])
# s = Student("zhangsan",18,"man","1056@qq.com")
#
# print isinstance(s,tuple)

# 如何统计出序列中元素的出现频度
# 1.某随机序列[2,3,4,..]中,找到c出现次数z最高的3个元素,他们的次数是多少
# from random import randint
# from collections import Counter
# data = [ randint(0,20) for _ in xrange(30)]
# print Counter(data).most_common(3)

# 2.对某英语单词,进行词频统计,找出次数出现最高的10个单词,他们出现的次数是多少
# import re
# from collections import Counter
#
# with open("word.txt", 'r') as fd:
#     txt_str = fd.read()
#     data = re.split('\W+', txt_str)
#     print Counter(data).most_common(10)

# 如何根据字典中值的大小,对字典中的项进行排序
# 案例:某班y英语成绩以字典形式储存为{"zhangsan":19,"lisi":20....},根据成绩的高低,计算学生的姓名
from random import randint

data = {x: randint(20, 100) for x in 'xyzasb'}
# 方案1
# print list(iter(data))
# data1 = zip(data.values(),data.keys())
# data1 = zip(data.itervalues(),data.iterkeys())
# print sorted(data1)
# 方案2
print sorted(data.items(), key=lambda x: x[1])
