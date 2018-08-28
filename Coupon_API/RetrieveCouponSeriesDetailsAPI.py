#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Common.Urls import URLS
from Utilities import datetimeformat

def RetrieveCouponSeriesDetails(userid):
    # 接口的url
    preUrl = URLS["url_MD5"]
    url = "%sv1.1/customer/coupons?format=json&id=%s" % (preUrl,userid)
    print(url)
    Auth = (Headers.AUTHS["kolon_demo"]["Username"],Headers.AUTHS["kolon_demo"]["Password"])
    Header = Headers.HEADERS1["Headers_MD5"]
    r = requests.request("get", url,auth=Auth, headers = Header)
    resp = json.loads(r.text)
    if resp["response"]["status"]["code"] == 200:
        count = (str(resp["response"]["customers"]["customer"][0]["coupons"]["coupon"]).count('series_id'))
        L1 = [];L2 = [];L3 = [];
        for i in range(0,count):
            coupon_code = resp["response"]["customers"]["customer"][0]["coupons"]["coupon"][i]["code"]
            redeemed = resp["response"]["customers"]["customer"][0]["coupons"]["coupon"][i]["redemption_count"]
            valid_till = resp["response"]["customers"]["customer"][0]["coupons"]["coupon"][i]["valid_till"]
            if valid_till < datetimeformat.getCurrentDateTime() and redeemed == 0:
                L1.append((coupon_code,valid_till))
            elif valid_till >= datetimeformat.getCurrentDateTime() and redeemed == 0:
                L2.append((coupon_code,valid_till))
            elif redeemed == 1:
                L3.append((coupon_code,valid_till))
        print('过期券', ' ', '过期日期')
        print(L1)
        print('未使用券', ' ', '过期日期')
        print(L2)
        print('已兑换的券', ' ', '过期日期')
        print(L3)

    elif resp["response"]["status"]["code"] == 500:
        print(resp["response"]["status"]["message"])
    elif resp["response"]["status"]["code"] == 400:
        print(resp["response"]["status"]["message"])
    else: print(resp)

def coupons_list(L=[]):
    L.append('END')
    return L

if __name__ == "__main__":
    RetrieveCouponSeriesDetails('339915126')
    RetrieveCouponSeriesDetails('33991512')
    RetrieveCouponSeriesDetails('')