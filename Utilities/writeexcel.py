#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlwt
from xlwt.compat import unicode, xrange
from openpyxl import Workbook
from xlutils.copy import copy
from Utilities import readexcel
'''
设置单元格样式
'''
#filename = "/pythonjulia/files/TNF Demo -- Fetch Transaction1.xls"

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def write_excel(filename, i, outputlist, start): # start 传的值是开始列
    oldWb = readexcel.read_excel(filename)
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)
    num = len(outputlist)

    for a in range(0, num):
        print("newWs.write(", i, start, a, outputlist[a], "set_style('Arial', 220, True))")
        newWs.write(i, start, outputlist[a], set_style('Arial', 220, True))
        for n in range(start + 1, num + start):
            print("newWs.write(", i, n, a + n - start, outputlist[a + n - start], "set_style('Arial', 220, True))")
            newWs.write(i, n, outputlist[a + n - start], set_style('Arial', 220, True))
        break

    print("write new values ok")
    newWb.save(filename)
    print("save with same name ok")

'''
def write_excel2(filename,i,Actual_code,Actual_message,birthday):
    oldWb = readexcel.read_excel(filename)
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)
    newWs.write(i, 3, Actual_code,set_style('Arial', 220, True))
    newWs.write(i, 4, Actual_message,set_style('Arial', 220, True))
    newWs.write(i, 5, birthday, set_style('Arial', 220, True))
    print("write new values ok")
    newWb.save(filename)
    print("save with same name ok")

def write_excel1(filename,i,Coupon_Code,Coupon_description,valid_till,discount_value):
    oldWb = readexcel.read_excel(filename)
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)
    newWs.write(i, 1, Coupon_Code,set_style('Arial', 220, True))
    newWs.write(i, 2, Coupon_description,set_style('Arial', 220, True))
    newWs.write(i, 3, valid_till, set_style('Arial', 220, True))
    newWs.write(i, 4, discount_value, set_style('Arial', 220, True))
    print("write new values ok")
    newWb.save(filename)
    print("save with same name ok")
'''