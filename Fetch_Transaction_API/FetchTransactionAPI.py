#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from Common import Headers
from Common import Urls


class FetchTransaction():
    # 接口的header
    #headers = Headers.HEADERS["tnf_demo"]
    filename = '/pythonjulia/files/TNF Demo -- Fetch Transaction2.xls'
    def FetchTransactionDetails(cellValues):
        # 接口的url
        preUrl = Urls.URLS["url2"]
        url = "%sv1.1/transaction/get?format=json&number=%s"% (preUrl,cellValues)
        r = requests.request("get", url, headers=Headers.HEADERS["tnf_demo"])
        status = r.status_code
        if status != 200:
            print ("\x1b[31mfail: status-> {} {}\x1b[0m".format(status, url))

        resp = json.loads(r.text)
        resp_code = resp["response"]["transactions"]["transaction"][0]["item_status"]["code"]
        resp_message = resp["response"]["transactions"]["transaction"][0]["item_status"]["message"]

        if resp_code== 600 and resp_message == "Transaction retrieved successfully":
            print("\x1b[32mpass: {}\x1b[0m".format(url))
        else:
            print("\x1b[31mfail: {} code: {}, message:{}\x1b[0m".format(url,resp_code,resp_message))
        #assert resp_code== 600 and resp_message == "Transaction retrieved successfully", "failed"
        return resp_code,resp_message

    getdata = readexcel.read_excel(filename)
    sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始
    #print(sheet1.name, sheet1.nrows, sheet1.ncols)

    for i in xrange(1,sheet1.nrows): #行数
           cellValues = sheet1.cell_value(i,0)
           print(cellValues)
           resp_code,resp_message=FetchTransactionDetails(cellValues)
           outputlist = [resp_code,resp_message]
           start = 3
           writeexcel.write_excel(filename,i,outputlist,start)

