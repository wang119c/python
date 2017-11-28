# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何为创建大量实例节省内存?

# 定义类的__slot__属性
#
# class Play(object):
#     __slots__ = ['uid', 'name', 'stat', 'level']
#
#     def __init__(self, uid, name, stat, level):
#         self.uid = uid
#         self.name = name
#         self.stat = stat
#         self.level = level


# 如何让对象支持上下文的管理?
# 需要定义__enter__,__exit__的方法
#
# with open('demo.txt', 'wb') as f:
#     f.write('aa')
#     f.writelines('213123')
# f.close()

# 如何创建可管理的对象属性?
# from math import pi
#
#
# class Circle(object):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def getRadius(self):
#         return self.radius
#
#     def setRadius(self, value):
#         self.radius = value
#
#     def getArea(self):
#         return self.radius ** 2 * pi
#
#     R = property(getRadius, setRadius)
# 如何让类支持比较操作?
# 方法一:
# class Ractangle(object):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def area(self):
#         return self.w * self.h
#
#     def __lt__(self, obj):
#         return self.area() < self.area()
#
#     def __le__(self, obj):
#         return self.area() <= self.area()
# 方法二:
# from functools import total_ordering
#
# @total_ordering
# class Ractangle(object):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def area(self):
#         return self.w * self.h
#
#     def __lt__(self, obj):
#         return self.area() < self.area()
#
#     def __eq__(self, obj):
#         return self.area() == self.area()
