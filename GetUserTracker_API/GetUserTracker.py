#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from Common import Headers

filename = "/pythonjulia/files/Descente Live -- Tracker.xls"

def GetUserTracker(cellValues):
        # 接口的url
        url = "https://api.capillarytech.cn.com/v2/customers/%s/trackers" % (int(cellValues))
        print(url)
        r = requests.request("get", url, headers=Headers.HEADERS["descente_live"])
        resp = json.loads(r.text)
        print(resp)
        trackerValue = resp["data"][0]["value"]
        print(trackerValue)
        outputlist = [trackerValue]
        return outputlist

getdata = readexcel.read_excel(filename)
sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始
    #print(sheet1.name, sheet1.nrows, sheet1.ncols)

for i in xrange(1, sheet1.nrows):  # 行数
        cellValues = sheet1.cell_value(i, 0)
        outputlist = GetUserTracker(cellValues)
        print(outputlist)
        start=1
        writeexcel.write_excel(filename,i,outputlist,start)


