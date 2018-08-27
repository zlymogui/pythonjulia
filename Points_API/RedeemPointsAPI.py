#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Common.Urls import URLS
from Utilities import datetimeformat

def RedeemPoints(points_redeemed,transaction_number,userid,notes,redemption_time):
    # 接口的url
    preUrl = URLS["url_MD5"]
    url = "%sv1.1/points/redeem?format=json" % preUrl
    print(url)

    body = "{\"root\":{\"redeem\":[{\"points_redeemed\":\"%s\"," \
           "\"transaction_number\":\"%s\"," \
           "\"customer\":{\"id\":\"%s\"}," \
           "\"notes\":\"%s\"," \
           "\"redemption_time\":\"%s\"}]}}" % (points_redeemed,transaction_number,userid,notes,redemption_time)
    print(body)

    Auth = (Headers.AUTHS["kolon_demo"]["Username"],Headers.AUTHS["kolon_demo"]["Password"])
    Header = Headers.HEADERS1["Headers_MD5"]
    r = requests.request("post", url, data=body.encode('utf-8'), auth=Auth, headers = Header)
    resp = json.loads(r.text)
    print(resp)
    assert resp["response"]["status"]["code"] ==200


if __name__ == "__main__":
    currentDateTime = datetimeformat.getCurrentDateTime()
    RedeemPoints('150','JULIA20180703001','339915126','积分抽奖321',currentDateTime)
