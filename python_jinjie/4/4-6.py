# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如何去掉z字符串中不需要的字符
# 方法一:
# s = ' ss  asd  das 2131 '
# print s.strip()
# print s.rstrip()
# print s.lstrip()
# s = '---ssda++'
# print s.strip('-+')

# 方法二:
# s = 'abc:123'
# print s[:3]+s[4:]

# 方法三:
# s = '\t123\tadasd\t3434\tff'
# print s.replace('\t','')

# s = '\tabc\t123\txyz\ropq\r'
# import re
# re.su
# re.subn
# re.sub('[\t\r]','',s)

s = 'abc123123xyz'
import string
print string.maketrans('abcxyz','xyzabc')





# 1.过滤掉用户输入的前后多余的空白字符

# 2.过滤掉windows下文本中的\r

# 3.去掉文本中unicode 组合符号(音调)


