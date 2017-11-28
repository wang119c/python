# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如何使用函数装饰器?
# def fibonacci(n, cache=None):
#     if cache is None:
#         cache = {}
#     if n in cache:
#         return cache[n]
#     if n <= 1:
#         return 1
#     cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
#     return cache[n]
# 方法
# def demo(func):
#     cache = {}
#
#     def wrap(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#
#     return wrap()
#
# @demo
# def fibonacci(n):
#     if n <= 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)


