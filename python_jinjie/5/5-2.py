# -*- coding: utf-8 -*-
import sys
import struct
import array

reload(sys)
sys.setdefaultencoding('utf8')

# 如何处理二进制文件
f = open('test.avi', 'rb')
info = f.read(44)
array.array('h', )
f.seek(0, 2)
f.tell()
n = (f.tell() - 44) / 2

buf = array.array('h', (0 for _ in xrange(n)))

f.seek(44)
f.readinto(buf)

for i in xrange(n): buf[i] /= 8

f2 = open('test2.avi', 'wb')
f2.write(info)
buf.tofile(f2)
f2.close()
#
# print struct.unpack('h',info[22:24])
