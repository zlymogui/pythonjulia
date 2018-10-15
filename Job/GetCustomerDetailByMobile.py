#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from GET_Customerid_API.GetCustomerId import GetCustomerIdAPI

filename = "/pythonjulia/files/TNF Live -- GetCustomerDetailsByMobile.xls"

getdata = readexcel.read_excel(filename)
sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始
for i in xrange(1, sheet1.nrows):  # 行数
    cellValues = sheet1.cell_value(i, 0)
    outputlist = GetCustomerIdAPI(cellValues)
    start = 1
    writeexcel.write_excel(filename, i, outputlist, start)