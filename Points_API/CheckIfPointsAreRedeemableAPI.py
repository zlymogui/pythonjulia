#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Common.Urls import URLS

def PointsRedeemable(userid,points):
    # 接口的url
    preUrl = URLS["url_MD5"]
    url = "%sv1.1/points/isredeemable?format=json&points=%s&id=%s" % (preUrl,points,userid)
    print(url)
    Auth = (Headers.AUTHS["kolon_demo"]["Username"],Headers.AUTHS["kolon_demo"]["Password"])
    Header = Headers.HEADERS1["Headers_MD5"]
    r = requests.request("get", url,auth=Auth, headers = Header)
    resp = json.loads(r.text)
    print(resp)
    assert resp["response"]["status"]["code"] ==200

if __name__ == "__main__":
    PointsRedeemable('339915126',100)
