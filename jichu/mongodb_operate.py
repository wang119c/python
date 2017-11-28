#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo
import datetime
import random

# 创建连接
client = pymongo.MongoClient('127.0.0.1', 27017)
# 操作数据库

db_name = 'lexing'
db = client[db_name]

collection_set01 = db['set01']

# 添加
###################--插入文档--####################
# save() vs insert()
# mongodb的save和insert函数都可以向collection里插入数据，但两者是有两个区别
# 1. save函数实际就是根据参数条件,调用了insert或update函数.如果想插入的数据对象存在,insert函数会报错,而save函数是改变原来的对象;如果想插入的对象不存在,那么它们执行相同的插入操作.这里可以用几个字来概括它们两的区别,即所谓"有则改之,无则加之".
# 2. insert可以一次性插入一个列表，而不用遍历，效率高， save则需要遍历列表，一个个插入.
# record_l = [
#     {'_id': 200, 'name': '1231', 'age': -27, 'high': 176},
#     {'_id': 201, 'name': '123', 'age': 27, 'high': 171},
#     {'_id': 202, 'name': 'sada', 'age': 26, 'high': 173},
#     {'_id': 203, 'name': 'fsdf', 'age': 29, 'high': 180},
#     {'_id': 204, 'name': 'gdfg', 'age': 30, 'high': 158},
#     {'_id': 205, 'name': 'asd', 'age': 22, 'high': 179},
#     {'_id': 206, 'name': 'zwasdj', 'age': 19, 'high': 166},
#     {'_id': 207, 'name': 'fghfg', 'age': 19, 'list': [2, 3, 5]},
#     {'_id': 208, 'name': 'zw,mnj', 'age': 19, 'list': [1, 2, 3, 4, 5, 6, 7]},
# ]
#
# try:
#     for record in record_l:
#         collection_set01.save(record)
# except pymongo.errors.DuplicateKeyError:
#     print 'record exists'
# except Exception as e:
#     print e


# 删除
####################--删除数据--####################
# remove()
# delete_one(self, filter, collation=None)
# delete_many(self, filter, collation=None)
# collection_set01.delete_many({'_id':{'$gt':6,'$lt':100}})   #删除所有满足条件的文档,删除_id大于6，小于100
# collection_set01.delete_one({'_id':6})   #删除一条满足条件的文档,删除_id=6
# #collection_set01.delete_many({}) #删除整个集合


# newinsert1 = {'_id':7,'comment':'test delete'}
# newinsert2 = {'_id':8,'comment':'test delete'}
# newinsert3 = {'_id':9,'comment':'test delete'}
# collection_set01.save(newinsert1)
# collection_set01.save(newinsert2)
# collection_set01.save(newinsert3)
#
# remove_before = collection_set01.find()
# print "delete before"
# for obj in remove_before :
#     print obj

# collection_set01.delete_many({'_id':{'$gt':6,'$lt':100}})
# remove_before = collection_set01.find()
# for obj in remove_before :
#     print obj


# collection_set01.delete_one({'_id':6})

# remove_before = collection_set01.find()
# for obj in remove_before:
#     print obj

# '''
# ###################--更新数据--####################
# replace_one(self, filter, replacement, upsert=False, bypass_document_validation=False, collation=None)
# update_one(self, filter, update, upsert=False, bypass_document_validation=False, collation=None)
# update_many(self, filter, update, upsert=False, bypass_document_validation=False, collation=None)
# '''
# collection_set01.replace_one({'_id': 1},{'comment': 'after replace_one operation just exists comment(key)'})　　#replace_one用指定的key-value替代原来所有的key-value
# collection_set01.update_one({ "high" : { '$gt' : 170 } } , { '$set' : { "comment" : "更新于身高高于170的一条记录"}}) #update_one更新已经对应的key-value，其它不变
# collection_set01.update_many({'high':{'$gt':171}},{'$set':{'comment':'use update_many'}})  #同上，能够update所有符合匹配条件的文档

# collection_set01.replace_one({'_id':1},{'comment': 'after replace_one operation just exists comment(key)'})
# print  collection_set01.find_one({'_id':1});

# collection_set01.update_one({'high': {'$gt': 170}}, {'$set': {'comment': '更新于身高高于170的一条记录'}})



# '''
# ########################--查询--###################
# find(self, filter=None, *args, **kwargs)
# find_one(self, filter=None, *args, **kwargs)
# params:projection/limit/skip
# '''
# #1.查询身高小于180的文档
# print '-------------身高小于180:'
# print type(collection_set01.find({'high':{'$lt':180}})) #<class 'pymongo.cursor.Cursor'>
# for r in collection_set01.find({'high':{'$lt':180}}):
#     print r
# print type(collection_set01.find_one({'high':{'$lt':180}})) #<type 'dict'>
# print 'use find_one:',collection_set01.find_one({'high':{'$lt':180}})['high']
# print 'use find_one:',collection_set01.find_one({'high':{'$lt':180}})
#
# #2.查询特定键(select key1,key2 from table;)
# print '-------------查询特定键--------'
# print '-------------查询身高大于170,并只列出_id,high和age字段(使用列表形式_id默认打印出来,可以使用{}忽视_id):'
# for r in collection_set01.find({'high':{'$gt':170}},projection=['high','age']):print r
# print '\n'
# print '--------------skip参数用法'
# for r in collection_set01.find({'high':{'$gt':170}},['high','age'],skip=1):print r #skip=1跳过第一个匹配到的文档
# for r in collection_set01.find({'high':{'$gt':170}},['high','age']).skip(1):print r #skip=1跳过第一个匹配到的文档
# print '\n'
# print '--------------limit参数用法'
# for r in collection_set01.find({'high':{'$gt':170}},['high','age'],limit=1):print r #limit=2限制显示2条文档
# print '\n'
# print '--------------用{}描述特定键'
# for r in collection_set01.find({'high':{'$gt':170}},{'high':1,'age':1,'_id':False}):print r
#
# print '---------------------多条件查询'
# print collection_set01.find_one({'high':{'$gt':10},'age':{'$lt':26,'$gt':10}})
#
# #3.$in
# print '----------------IN'
# for r in collection_set01.find({"age":{"$in":[23, 26, 32]}}): print r  # select * from users where age in (23, 26, 32)
# #for u in db.users.find({"age":{"$nin":(23, 26, 32)}}): print u # select * from users where age not in (23, 26, 32)
#
# #4.count统计数目
# print '----------------count'
# print collection_set01.find({"age":{"$gt":20}}).count() # select count(*) from set01 where age > 10
#
# #5.$or
# print '----------------条件或'
# print '大于等于29或者小于23'
# for r in collection_set01.find({"$or":[{"age":{"$lte":23}}, {"age":{"$gte":29}}]}): print r
#
# #6.$exists，是否存在字段
# print '------------exists'
# for r in collection_set01.find({'age':{'$exists':True}}):print 'age exists',r # select * from 集合名 where exists 键1
# for r in collection_set01.find({'age':{'$exists':False}}):print 'age not exists',r # select * from 集合名 where not exists 键1
#
# #7.正则表达式查询
# print '正则表达式查询'
# #method 1
# for r in collection_set01.find({'name':{'$regex':r'.*wei.*'}}):print r   #找出name字段中包含wei的文档
# #method 2
# import re
# Regex = re.compile(r'.*zhang.*',re.IGNORECASE)
# for r in collection_set01.find({'name':Regex}):print r   #找出name字段中包含wei的文档
#
#
# #8.sort排序
#
# print '--------------------使用sort排序(文档中没有排序的字段也会打印出来,表示最小)'
# #pymongo.ASCENDING      1
# #pymongo.DESCENDING     -1
# #sort([[],()]),[],()均可
# print '--------------age 升序'
# for r in collection_set01.find().sort([["age",pymongo.ASCENDING]]):print r
# print '--------------age 降序'
# for r in collection_set01.find().sort([("age",-1)]):print r
# print '--------------age升序,high升序'
# for r in collection_set01.find().sort((("age",pymongo.ASCENDING),("high",pymongo.ASCENDING))):print r
# print '--------------age升序，high降序'
# for r in collection_set01.find(sort=[("age",pymongo.ASCENDING),("high",pymongo.ASCENDING)]):print r
#
#
# #9.$all判断数组属性是否包含全部条件,注意与$in区别
#
# print '-------------$all'
# for r in collection_set01.find({'list':{'$all':[2,3,4]}}):print r
# print '-------------$in'
# for r in collection_set01.find({'list':{'$in':[2,3,4]}}):print r
#
#
# #10.$size匹配数组属性元素数量
# print '-------------$size'
# print '-------------size=3'
# for r in collection_set01.find({'list':{'$size':3}}):print r
# print '-------------size=7'
# for r in collection_set01.find({'list':{'$size':7}}):print r
#
# #11.$unset和$set相反表示移除文档属性
# print '-------------------$unset'
# print '---before'
# for r in collection_set01.find({'name':'weijian'}):print r
# collection_set01.update({'name':'weijian'},{'$unset':{'age':1}})
# print '---after'
# for r in collection_set01.find({'name':'weijian'}):print r
# print collection_set01.find({'age':{'$gt':20}}).count()

