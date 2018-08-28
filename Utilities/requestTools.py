#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import datetimeformat
import requests
import json
from Common import Headers
from Common import Urls

def requestPrepare(brandEnv,headPswType,urlType):
    auth = (Headers.AUTHS[brandEnv]["Username"], Headers.AUTHS[brandEnv]["Password"])
    header = Headers.HEADERS1[headPswType]
    preUrl = Urls.URLS[urlType]
    return auth,header,preUrl

def requestPrepareWithDiffTill(till,brandEnv,headPswType,urlType):
    auth = (till, Headers.AUTHS[brandEnv]["Password"])
    header = Headers.HEADERS1[headPswType]
    preUrl = Urls.URLS[urlType]
    return auth,header,preUrl

def requestPOST(url,bodyjson,header,auth):
    body = json.dumps(bodyjson, ensure_ascii=False)
    r = requests.request("post", url, data=body.encode('utf-8'), headers=header, auth=auth)
    resp = json.loads(r.text)
    return resp

def generateOrderNumber():
    orderNumber = 'JULIA'+ datetimeformat.getCurrentDateTimef1()
    return orderNumber