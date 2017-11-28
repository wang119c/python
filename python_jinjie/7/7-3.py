# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如何使用描述符对实例属性做类型检查?
# 分别实现__set__,__get__,__delete__方法,在__set__内使用isinstace函数z做类型检查

# class Attr(object):
#     def __init__(self, name, type_):
#         self.name = name
#         self.type_ = type_
#
#     def __get__(self, instance, cls):
#         print 'in __get__', instance, cls
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self.type_):
#             raise TypeError("ddd" + self.type_)
#         print 'in __set__'
#         instance.__dict__[self.name] = value
#
#     def __delete__(self, instance):
#         print  "in __delete__"
#         del instance.__dict__[self.name]
#
#
# class Person(object):
#     name = Attr('name', str)
#     age = Attr('age', int)
#     height = Attr('height', int)

# 如何在环状数据结构中管理内存?
# 可以使用弱引用,weakref
# import weakref
#
# weakref.ref(a)


# 如何通过谁方法名称字符串调用方法?

