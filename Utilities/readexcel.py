#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
import files

#filename = "/pythonjulia/files/TNF Demo -- Fetch Transaction1.xls"
#filename = "/pythonjulia/files/Descente Demo -- Issue Coupon.xls"

def read_excel(filename):
    # 打开文件
    workbook = xlrd.open_workbook(filename,formatting_info=True)
    return workbook