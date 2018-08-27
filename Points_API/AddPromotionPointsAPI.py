#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Common.Urls import URLS

def IssuePoints(userid,points):
    # 接口的url
    preUrl = URLS["url_MD5"]
    url = "%sv1.1/request/add?client_auto_approve=true&format=json" % preUrl
    print(url)

    body = "{\"root\":{\"request\":[{\"customer\":{\"id\":\"%s\"}," \
           "\"comments\":\"API Service request - Awarding him %s points.\"," \
           "\"reason\":\"POINTS_ISSUE\",\"type\":\"GOODWILL\",\"base_type\":\"POINTS\"," \
           "\"points\":\"%s\"}]}}" % (userid,points,points)
    Auth = (Headers.AUTHS["kolon_demo"]["Username"],Headers.AUTHS["kolon_demo"]["Password"])
    Header = Headers.HEADERS1["Headers_MD5"]
    r = requests.request("post", url, data=body, auth=Auth, headers = Header)
    resp = json.loads(r.text)
    print(resp)
    assert resp["response"]["status"]["code"] ==200


if __name__ == "__main__":
    IssuePoints('339915126',100)
