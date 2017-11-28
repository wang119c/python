# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 如何读写excel 文件工作簿1.xlsx
import xlrd,xlwt
rbook = xlrd.open_workbook('test.xlsx')
# print book.sheets()
# sheet = book.sheet_by_index(0)
# print sheet

rsheet = rbook.sheet_by_index(0)
nc = rsheet.ncols
rsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,'总分',None)
for row in xrange(1,rsheet.nrows):
    pass