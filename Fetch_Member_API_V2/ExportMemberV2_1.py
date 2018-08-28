#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange
from Common import Headers
from Common import Urls

class ExportMemberV2_1():

    def ExportMemberV2_1Details(userId):
        # 接口的url
        preUrl = Urls.URLS["tnf_demo"]["url"]
        source = Urls.URLS["tnf_demo"]["source3"]
        url = "%sv2/customers/%s?source=%s&embed=points" % (preUrl,userId,source)
        print(url)
        r = requests.request("get", url, headers=Headers.HEADERS["tnf_demo"])
        resp = json.loads(r.text)
        print(resp)
        fields=resp["profiles"][0]["fields"]
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
        print('---')
        print(resp["profiles"])
        #resp_firstName = resp["profiles"][0]["firstName"]
        resplist=[userId,resp_mobile,resp_externalId,resp_bday,resp_tnflastupdate,resp_gender]
        #print(resplist)
        #print(len(resplist))
        return resplist

