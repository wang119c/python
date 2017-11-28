# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如何使用临时文件
# 实际案例:
# 某项目中,我们从传感器采集数据,m每收集1G数据后,z做数据分析,我们可以使用临时文件存储这些数据 ,临时文件不用命名,且关闭h后自动删除

from tempfile import  TemporaryFile,NamedTemporaryFile
# f = TemporaryFile()
# f.write('adasdas'*10000000)
# f.seek(0)
# print f.read(100)

ntf = NamedTemporaryFile()
print ntf.name
