#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Common import Urls
from Fetch_Member_API_V2.ExportMemberV2_1 import ExportMemberV2_1

def GetCustomerIdAPI(mobile):
        # 接口的url
        preUrl = Urls.URLS["tnf_demo"]["url"]
        url = "%sv2/customers/search?q=%s" % (preUrl,mobile)
        print(url)
        r = requests.request("get", url, headers=Headers.HEADERS["tnf_demo"])
        resp = json.loads(r.text)
        if resp["pagination"]["total"] ==1:
            userId = resp["data"][0]["userId"]
            print(userId)
            resplist = ExportMemberV2_1.ExportMemberV2_1Details(userId)

        else:
            print(mobile,"This mobile has more than one userid")
            resplist = ["This mobile has more than one userid"]
        return resplist








