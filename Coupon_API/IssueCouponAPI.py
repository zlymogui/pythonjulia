#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange

filename = "/pythonjulia/files/TNF -- Issue Coupon.xls"

# 接口的header
headers = Headers.HEADERS["tnf_demo"]
getdata = readexcel.read_excel(filename)
sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始

def IssueCoupon():
    # 接口的url
    url = "https://apichina.capillarytech-cn.com/api/v1.1/coupon/issue?format=json"
    for i in xrange(1, sheet1.nrows):  # 行数
        series_id = int(sheet1.cell_value(i,0))
        user_id = int(sheet1.cell_value(i,1))
        body = "{\"root\":{\"coupon\":[{\"series_id\":\"%s\",\"customer\":{\"id\":\"%s\"}}]}}" % (series_id,user_id)
        print(body)
        r = requests.request("post", url, data=body, headers=headers)
        resp = json.loads(r.text)
        #print(resp)
        resp_code = resp["response"]["status"]["code"]
        if resp_code == 200:
            coupon_code = resp["response"]["coupon"]["code"]
            coupon_desc = resp["response"]["coupon"]["description"]
            coupon_valid_till = resp["response"]["coupon"]["valid_till"]
            coupon_discount_value = resp["response"]["coupon"]["discount_value"]
            resplist = [coupon_code,coupon_desc,coupon_valid_till,coupon_discount_value,resp_code]
            print(coupon_code)
            print(coupon_desc)
            print(coupon_valid_till)
            print(coupon_discount_value)
        else:
            print(resp)
            resp_code = resp['response']['status']['code']
            resp_message = resp['response']['status']['message']
            resplist = [resp_code,resp_message]
        start = 3
        writeexcel.write_excel(filename, i, resplist, start)

if __name__ == "__main__":
    IssueCoupon()
