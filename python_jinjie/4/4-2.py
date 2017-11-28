# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何判断字符串a是否以字符串b开头或结尾?
# import os, stat
# print [name for name in os.listdir('./test/') if name.endswith(('.py','.c'))]
# 如何调整z字符串中文本的格式?
import re
s = open('word.txt')
c = s.read()
# print re.sub('(\d{4})-(\d{2})-(\d{2})',r'\1/\2/\3',c)
print  re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<year>/\g<month>/\g<day>',c)