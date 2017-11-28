# -*- coding: utf-8 -*-
# 如何快速找出多个字典中的公共键
# 案例  {"梅西":1,"c罗":2} {"梅西":2,"c罗11":4}... 取出这几场比赛都要进球人员的
from random import randint, sample

q1 = sample('abcdefg', 3)
q2 = sample('abcdefg', randint(3, 6))
qs1 = {x: randint(1, 4) for x in q1}
qs2 = {x: randint(1, 4) for x in q1}
qs3 = {x: randint(1, 4) for x in q2}

# 解决方案1 有限的字典中
# print  qs1.viewkeys() & qs2.viewkeys() & qs3.viewkeys()
# 解决方案2 无限的字典中
map1 = map(dict.viewkeys, [qs1, qs2, qs3])
print reduce(lambda a, b: a & b, map1)
