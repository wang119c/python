# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如何访问文件的状态?
# 实际案例:在某些项目中获得文件的状态,如:1.文件类型 2 . 文件的权限 3.文件的最后修改时间 4.大小
# 第一种用os
# 第二种用os.path下的函数,会用起来更简洁
import os
import stat
import time
# s = os.stat('word.txt')
# print stat.S_ISDIR(s.mode)
print time.localtime()