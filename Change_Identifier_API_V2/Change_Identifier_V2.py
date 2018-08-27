#!/usr/bin/python
# -*- coding: UTF-8 -*-
# birthday,gender,city

import requests
import json
from Common import Headers
from Common import Urls
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from Utilities import datetimeformat


filename = '/pythonjulia/files/TNF live -- change identifier.xls'

def Change_Identifier():
        # 接口的url
        headers = Headers.HEADERS["tnf_live_import"]
        preUrl = Urls.URLS["tnf_live"]["url"]
        source = Urls.URLS["tnf_live"]["source2"]
        getdata = readexcel.read_excel(filename)
        sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始
        print(sheet1)
        for i in xrange(1, sheet1.nrows):  # 行数
            accountId = sheet1.cell_value(i, 9)
            userid = sheet1.cell_value(i, 12)
            url = "%sv2/customers/%s/changeIdentifier?source=%s&accountId=%s" % (preUrl, userid,source, accountId)
            print(url)
            mobile = sheet1.cell_value(i, 1)
            externalId = sheet1.cell_value(i, 3)
            #openid = sheet1.cell_value(i, 7)
            body = "{\"add\": [{\"type\": \"externalId\", \"value\": \"%s\"}, {\"type\": \"mobile\", \"value\": \"%s\"}]}" % (externalId, mobile)
            print(body)
            r = requests.request("post", url, data=body.encode('utf-8'), headers=headers)
            print(r)
            resp = json.loads(r.text)
            print(resp)
            if "createdId" in resp and "code" not in resp:
                userid = resp["createdId"]
                outputlist = [userid]
            elif "createdId" in resp and "code" in resp:
                userid = resp["createdId"]
                code = resp["warnings"][0]["code"]
                status = resp["warnings"][0]["status"]
                message = resp["warnings"][0]["message"]
                outputlist=[userid,code,status,message]
            else:
                code = resp["errors"][0]["code"]
                status = resp["errors"][0]["status"]
                message = resp["errors"][0]["message"]
                outputlist=[code,status,message]
            print(outputlist)
            print(len(outputlist))
            start = 13
            writeexcel.write_excel(filename, i, outputlist, start)

Change_Identifier()










