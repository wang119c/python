# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


from functools import update_wrapper,wraps
# 如何为被装饰的函数保存元数据?
def mydecorator(func):
    def wrapper(*args, **kargs):
        print 'In wrapper'
        func(*args, **kargs)
    update_wrapper(wrapper,func,('__name__','__doc__'))
    return wrapper

@mydecorator
def example():
    print 'in example'

print example.__doc__
print example.__name__