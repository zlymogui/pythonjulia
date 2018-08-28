#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from Common import Headers
from Common import Urls

filename = "/pythonjulia/files/Mergelist.xls"

def retrieve_userid_by_mobile(mobile):
        # 接口的url
        preUrl = Urls.URLS["url_SHA256"] #WECHAT-gh_07d2c13f29a2
        url = "%sv2/customers/lookup?source=WECHAT&accountId=gh_07d2c13f29a2&identifierName=mobile&identifierValue=%s" % (preUrl,mobile)
        print(url)
        r = requests.request("get", url, headers=Headers.HEADERS["tnf_demo"])
        resp = json.loads(r.text)
        print(resp)

        if "entity" in resp:
            userid = resp["entity"]
            resplist=[userid]
        else:
            resplist = [str(resp)]
        return resplist

getdata = readexcel.read_excel(filename)
sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始

for i in xrange(1, sheet1.nrows):  # 行数
    cellValues = sheet1.cell_value(i, 0)
    outputlist = retrieve_userid_by_mobile(cellValues)
    start=1
    writeexcel.write_excel(filename,i,outputlist,start)

