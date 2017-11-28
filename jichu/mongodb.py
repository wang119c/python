#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient

# 连接mongodb数据库
client = MongoClient('mongodb://127.0.0.1:27017/');
# 指定数据库的名称
db = client.lexingziyuan
# 获取非系统的集合
db.collection_names(include_system_collections=False)
# 获取集合名
posts = db.posts
# 查找单个文档
posts.find_one()
#给定条件的一个文档
posts.find_one({"author": "Mike"})