#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
import files
from openpyxl import Workbook

filename = "/pythonjulia/files/TNF Demo -- Advance search_2.xlsx"
#filename = "/pythonjulia/files/Descente Demo -- Issue Coupon.xls"

def read_excel(filename):
    # 打开文件
   # workbook = xlrd.open_workbook(filename,formatting_info=True)

    workbook = Workbook()
    booksheet = workbook.active     #获取当前活跃的sheet,默认是第一个sheet
    #存第一行单元格cell(1,1)
    booksheet.cell(1,1).value = 6   #这个方法索引从1开始
    booksheet.cell.value = 7
    #存一行数据
    booksheet.append([11,87])
    workbook.save(filename)
    return workbook


read_excel(filename)