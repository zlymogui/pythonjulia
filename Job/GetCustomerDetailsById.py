#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from Fetch_Member_API_V2.ExportMemberV2_1 import ExportMemberV2_1

filename = "/pythonjulia/files/TNF Demo -- GetCustomerDetailsById.xls"

getdata = readexcel.read_excel(filename)
sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始
for i in xrange(1, sheet1.nrows):  # 行数
    cellValues = sheet1.cell_value(i, 0)
    outputlist = ExportMemberV2_1.ExportMemberV2_1Details(cellValues)
    start = 1
    writeexcel.write_excel(filename, i, outputlist, start)