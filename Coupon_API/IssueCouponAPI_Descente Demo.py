#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Utilities import readexcel
from Utilities import writeexcel
from xlrd.timemachine import xrange

filename = "/pythonjulia/files/Descente Demo -- Issue Coupon_total_2.xls"

# 接口的header
headers = Headers.HEADERS["kolon_live"] # 如果是别的品牌，那要去Common文件夹下的Headers.py下面把品牌till加上， TNF的话用IssueCouponAPI.py因为API的url不一样
getdata = readexcel.read_excel(filename)
sheet1 = getdata.sheet_by_index(0)  # sheet索引从0开始
print(sheet1)

def DescenteIssueCoupon():
    # 接口的url
    url = "https://api.capillarytech.cn.com/v1.1/coupon/issue?format=json"
    for i in xrange(1, sheet1.nrows):  # 行数
        body = sheet1.cell_value(i, 0)
        print(body)
        r = requests.request("post", url, data=body, headers=headers)
        resp = json.loads(r.text)
        print(resp)
        resp_code = resp["response"]["status"]["code"]
        coupon_code = resp["response"]["coupon"]["code"]
        coupon_desc = resp["response"]["coupon"]["description"]
        coupon_valid_till = resp["response"]["coupon"]["valid_till"]
        coupon_discount_value = resp["response"]["coupon"]["discount_value"]
        resplist = [coupon_code,coupon_desc,coupon_valid_till,coupon_discount_value,resp_code]
        if resp_code == 200:
            print(coupon_code)
            print(coupon_desc)
            print(coupon_valid_till)
            print(coupon_discount_value)
            start=1 # 从excel的第2列开始写入，excel第一列是0
            writeexcel.write_excel(filename,i, resplist,start)
        else: print(resp)

if __name__ == "__main__":
    DescenteIssueCoupon()
