# -*- coding: utf-8 -*-
# 如何实现用户的历史记录功能?
# 实际案例:
# 我们制作了一个j简单的猜数字游戏,添加历史记录功能,显示用户最近猜过的数字,如何实现?
# 解决方案使用队列
from collections import deque
from random import randint
import pickle

N = randint(0, 100)
print N
history = deque([], 5)


def guess(k):
    if k == N:
        print "right"
        return True
    elif k > N:
        print "Big"
        return False
    elif k < N:
        print "small"
        return False


while True:
    line = raw_input("input a number?\r\n")
    if line.isdigit():
        k = int(line)

        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print list(history)
pickle.dump(str(list(history)), open('history', 'w'))
print pickle.load(open('history'))
