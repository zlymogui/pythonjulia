#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Common.Urls import URLS

def PointsRedeemable(userid,coupon):
    # 接口的url
    preUrl = URLS["url_MD5"]
    url = "%sv1.1/coupon/isredeemable?format=json&details=true&code=%s&id=%s" % (preUrl,coupon,userid)
    print(url)
    Auth = (Headers.AUTHS["kolon_demo"]["Username"],Headers.AUTHS["kolon_demo"]["Password"])
    Header = Headers.HEADERS1["Headers_MD5"]
    r = requests.request("get", url,auth=Auth, headers = Header)
    resp = json.loads(r.text)
    #print(resp)
    #assert resp["response"]["status"]["code"] ==200
    if resp["response"]["status"]["code"]==200 and resp["response"]["coupons"]["redeemable"]["item_status"]["code"]==700:
        print(resp["response"]["coupons"]["redeemable"]["item_status"]["message"])#可以被核销
    elif resp["response"]["status"]["code"]==500 and resp["response"]["coupons"]["redeemable"]["item_status"]["code"]==711:
        print(resp["response"]["coupons"]["redeemable"]["item_status"]["message"])#已兑换
    elif resp["response"]["status"]["code"]==500 and resp["response"]["coupons"]["redeemable"]["item_status"]["code"]==713:
        print(resp["response"]["coupons"]["redeemable"]["item_status"]["message"])#已过期
    elif resp["response"]["status"]["code"]==500 and resp["response"]["coupons"]["redeemable"]["item_status"]["code"]==719:
        print(resp["response"]["coupons"]["redeemable"]["item_status"]["message"])#券不存在
    elif resp["response"]["status"]["code"]==500 and resp["response"]["coupons"]["redeemable"]["item_status"]["code"]==701:
        print(resp["response"]["coupons"]["redeemable"]["item_status"]["message"])#customer不存在
    elif resp["response"]["status"]["code"]==500 and resp["response"]["coupons"]["redeemable"]["item_status"]["code"]==710:
        print(resp["response"]["coupons"]["redeemable"]["item_status"]["message"])#券不是对应的customer的
    elif resp["response"]["status"]["code"]==400:
        print(resp["response"]["status"]["message"])#input is invalid
    else: print(resp)

if __name__ == "__main__":
    PointsRedeemable('339915126', '9IJ2Y6DE')# 激活700
    PointsRedeemable('339915126','N0ZG4RX0')#已兑换711
    PointsRedeemable('339915126','KY8BTQP3')#过期713
    PointsRedeemable('339915126','N0ZG4R0')# 719
    PointsRedeemable('339915127','MSDUKJ2P')# 701
    PointsRedeemable('339914421','MSDUKJ2P')# 710
