#!/usr/bin/python
# -*- coding: utf-8 -*-

from openpyxl import load_workbook

def read_excel(filename,sheetname):
    # 打开一个workbook
    wb = load_workbook(filename)
    # 获取所有表格(worksheet)的名字
    sheets = wb.sheetnames
    # 第一个表格的名称
    sheet_first = sheets[0]
    # 获取特定的worksheet
    ws = wb[sheetname]
    ncol = ws.max_column
    nrow = ws.max_row

    return ws,ncol,nrow


'''
        for tType in range(2, tn+2):  # 行数
            transaction_type1 = ws.cell(row=tType, column=11).value
            transaction_type2 = ws.cell(row=tType+1, column=11).value
            if transaction_type1 != transaction_type2:
                print(tType,tType+1,transaction_type1)
            else:
                break
    else:
        break
'''


'''
    for i in range(1, nrow+1):  # 行数
        for j in range(1,ncol+1):
            print("ws.cell(row=",i,", column=",j,").value")
            print(ws.cell(row=i, column=j).value)
    print('--- END OF ROW ---')
'''
'''
    # 获取表格所有行和列，两者都是可迭代的
    rows = ws.rows
    columns = ws.columns
    
    # 迭代所有的行
    for row in rows:
        line = [col.value for col in row]
        print(line)

    for row in ws.iter_rows():
        for cell in row:
            print(cell.coordinate, cell.value)
    print('--- END OF ROW ---')
    # 通过坐标读取值
    #print(ws.cell('A1').value)  # A表示列,1表示行
    print(ws.cell(row=1, column=1).value)
'''
#filename = "/pythonjulia/files/nonmember_SR.xlsx"
#sheetname = 'sheet1'
#read_excel(filename,sheetname)