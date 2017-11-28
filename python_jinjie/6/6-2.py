# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如歌读取json数据?
import json

j = [1,2,3,4,{'aa':'bb'}]

print  json.dumps(j)

# 解析字符串
json.loads()
