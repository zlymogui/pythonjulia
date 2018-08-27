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
    url = "https://apichina.capillarytech-cn.com/api/v1.1/coupon/redeem?format=json"
    for i in xrange(1, sheet1.nrows):  # 行数
        coupon_code = sheet1.cell_value(i,3)
        user_id = int(sheet1.cell_value(i,1))
        trans_number = sheet1.cell_value(i,2)
        body = "{\"root\":{\"coupon\":[{\"code\": \"%s\",\"customer\":{\"id\":\"%s\"},\"transaction\":[{\"number\":\"%s\",\"amount\":\"300\"}]}]}}" % (coupon_code,user_id,trans_number)
        print(body)
        r = requests.request("post", url, data=body, headers=headers)
        resp = json.loads(r.text)
        print(resp)
        resp_code = resp["response"]["status"]["code"]
        resp_message = resp["response"]["status"]["message"]
        resplist = [resp_code,resp_message]
        start=8
        writeexcel.write_excel(filename, i, resplist, start)


if __name__ == "__main__":
    IssueCoupon()
