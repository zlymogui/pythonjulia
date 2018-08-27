#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Common.Urls import URLS

def CashCouponValidation(billamount,coupon,card_number,mobile):
    # 接口的url
    url = "http://adapterconfig.capillarytech.cn.com/api/descente/discountvalidation"
    Auth = (Headers.AUTHS["kolon_demo"]["Username"],Headers.AUTHS["kolon_demo"]["Password"])
    Header = Headers.HEADERS1["Headers_MD5"]
    body = "{\"bill_amount\":\"%s\"," \
           "\"coupon_code\":\"%s\"," \
           "\"card_number\":\"%s\"," \
           "\"mobile\":\"%s\"}"% (billamount,coupon,card_number,mobile)
    r = requests.request("post", url,auth=Auth, headers=Header,data=body)
    resp = json.loads(r.text)
    if resp["response"]["status"]=="1000":
        print(resp["response"]["message"])
        print(resp["response"]["bill_amount"])
        print(resp["response"]["discount_value"])
    elif resp["response"]["status"]=="500":
        print(resp["response"]["message"])
    #else: print(resp)

if __name__ == "__main__":
    CashCouponValidation('1000', 'MSDUKJ2P','','18221426687')
    CashCouponValidation('1000', '9IJ2Y6DE','','18221426687')
    CashCouponValidation('1000', 'MSDUKJ2P','','18221426686')
    CashCouponValidation('1000', 'MSDUKJ2P','','')
