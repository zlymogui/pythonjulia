#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from Common import Headers
from Common import Urls

class ExportMemberV2():

    filename = "/pythonjulia/files/TNF Demo -- Fetch Transaction1.xls"

    def ExportMemberV2Details(cellValues):
        # 接口的url
        preUrl = Urls.URLS["tnf_demo"]["url"]
        source = Urls.URLS["tnf_demo"]["source"]
        accountId = Urls.URLS["tnf_demo"]["accountId"]
        url = "%sv2/customers/%s?source=%s&accountId=%s" % (preUrl,cellValues,source,accountId)
        print(url)
        r = requests.request("get", url, headers=Headers.HEADERS["tnf_demo"])
        resp = json.loads(r.text)
        fields=resp["profiles"][0]["fields"]
        #print(fields)
        resp_bday = ''
        resp_tnflastupdate = ''
        resp_gender=''
        if "birthday" in fields:
             resp_bday = fields['birthday']
        if "tnflastupdate" in fields:
             resp_tnflastupdate = fields['tnflastupdate']
        if "gender" in fields:
             resp_gender = fields['gender']

        resp_mobile = '',
        resp_externalId=''
        for i in resp["profiles"][0]["identifiers"]:
             if i["type"]=="mobile":
                 resp_mobile = i["value"]
             if i["type"] == "externalId":
                 resp_externalId = i["value"]
        resplist=[resp_mobile,resp_externalId,resp_bday,resp_tnflastupdate,resp_gender]
        return resplist

    getdata = readexcel.read_excel(filename)
    sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始
    #print(sheet1.name, sheet1.nrows, sheet1.ncols)

    for i in xrange(1, sheet1.nrows):  # 行数
        cellValues = sheet1.cell_value(i, 0)
        #resp_mobile, resp_externalId, resp_bday = ExportMemberV2Details(cellValues)
        outputlist = ExportMemberV2Details(cellValues)
        start=1
        writeexcel.write_excel(filename,i,outputlist,start)
        

