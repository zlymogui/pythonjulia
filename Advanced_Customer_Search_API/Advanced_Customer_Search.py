#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from Common import Headers

filename = "/pythonjulia/files/TNF Demo -- Advance search_1.xls"

def Advanced_Customer_Search(cellValues):
        # 接口的url
        url = "https://apichina.capillarytech-cn.com/api/v2/customers/search?q=%s" % (cellValues)
        r = requests.request("get", url, headers=Headers.HEADERS["tnf_demo"])
        resp = json.loads(r.text)

        total_count= resp["pagination"]["total"]
        data = []
        userStr=""
        for m in range(0,total_count):
            data.append(resp["data"][m]["userId"])
            userStr=userStr+str(resp["data"][m]["userId"])+" "

        resplist=[cellValues,total_count,userStr]
        return resplist

getdata = readexcel.read_excel(filename)
sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始
    #print(sheet1.name, sheet1.nrows, sheet1.ncols)

for i in xrange(1, sheet1.nrows):  # 行数
        cellValues = sheet1.cell_value(i, 0)
        outputlist = Advanced_Customer_Search(cellValues)
        print(outputlist)
        start=1
        writeexcel.write_excel(filename,i,outputlist,start)


