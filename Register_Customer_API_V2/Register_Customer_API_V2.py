#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Common import Urls
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from Utilities import datetimeformat
import time

filename = '/pythonjulia/files/TNF Demo -- Register Customer.xls'

def RegisterWeChat():
        # 接口的url
        headers = Headers.HEADERS["tnf_demo_wechat"]
        preUrl = Urls.URLS["tnf_demo"]["url"]
        source = Urls.URLS["tnf_demo"]["source2"]
        getdata = readexcel.read_excel(filename)
        sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始

        for i in xrange(1, sheet1.nrows):  # 行数
            accountId = sheet1.cell_value(i, 9)
            url = "%sv2/customers?source=%s&accountId=%s" % (preUrl, source, accountId)
            print(url)
            email = sheet1.cell_value(i, 0)
            mobile = sheet1.cell_value(i, 1)
            createDateS = sheet1.cell_value(i, 2)
            if createDateS != '':
                createDate = datetimeformat.string_toDatetime(createDateS)
            else: createDate = ''
            externalId = sheet1.cell_value(i, 3)
            firstName = sheet1.cell_value(i, 4)
            birthdayS = sheet1.cell_value(i, 5)
            if birthdayS != '':
                birthday = datetimeformat.string_toDate(birthdayS)
            else: birthday = ''
            gender = sheet1.cell_value(i, 6)
            openid = sheet1.cell_value(i, 7)
            if email != ''and firstName !='' and birthday !='' and gender != '':
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"fields\":{\"gender\":\"%s\",\"birthday\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (firstName, gender, birthday, openid, mobile, externalId, email, openid, mobile, createDate)
            elif email == ''and firstName !='' and birthday !='' and gender != '':
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"fields\":{\"gender\":\"%s\",\"birthday\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (firstName, gender, birthday, openid, mobile, externalId, openid, mobile, createDate)
            elif email == ''and firstName =='' and birthday !='' and gender != '':
                body = "{\"profiles\":[{\"fields\":{\"gender\":\"%s\",\"birthday\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (gender, birthday, openid, mobile, externalId, openid, mobile, createDate)
            elif email == ''and firstName =='' and birthday =='' and gender != '':
                body = "{\"profiles\":[{\"fields\":{\"gender\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (gender, openid, mobile, externalId, openid, mobile, createDate)
            elif email == ''and firstName =='' and birthday =='' and gender == '':
                body = "{\"profiles\":[{\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (openid, mobile, externalId, openid, mobile, createDate)
            elif email != ''and firstName =='' and birthday !='' and gender != '':
                body = "{\"profiles\":[{\"fields\":{\"gender\":\"%s\",\"birthday\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (gender, birthday, openid, mobile, externalId, email, openid, mobile, createDate)
            elif email != ''and firstName =='' and birthday =='' and gender != '':
                body = "{\"profiles\":[{\"fields\":{\"gender\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % ( gender, openid, mobile, externalId, email, openid, mobile, createDate)
            elif email != ''and firstName =='' and birthday =='' and gender == '':
                body = "{\"profiles\":[{\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (openid, mobile, externalId, email, openid, mobile, createDate)
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
                print(type(userid))
                print(type(code))
                print(type(status))
                print(type(message))
            else:
                code = resp["errors"][0]["code"]
                status = resp["errors"][0]["status"]
                message = resp["errors"][0]["message"]
                outputlist=[code,status,message]
            start = 11
            writeexcel.write_excel(filename, i, outputlist, start)

RegisterWeChat()