#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Utilities import readjson

# 接口的header
headers = Headers.HEADERS["purples"]
filename='/pythonjulia/files/AddTransactionRequestBody.json'
body = readjson.read_json(filename)
print(body)

def AddTransactionDetails():
    # 接口的url
    url = "https://api.capillarytech.cn.com/v1.1/transaction/add?format=json"
    #r = requests.post(url, data = body,headers=headers)
    r = requests.request("post", url, data = body,headers=headers)
    resp = json.loads(r.text)
    print(resp)

    status = r.status_code
    if status != 200:
        print ("\x1b[31mfail: status-> {} {}\x1b[0m".format(status, url))

    resp = json.loads(r.text)
    resp_code = resp["response"]["transactions"]["transaction"][0]["item_status"]["code"]
    resp_message = resp["response"]["transactions"]["transaction"][0]["item_status"]["message"]
    transcation_number = resp["response"]["transactions"]["transaction"][0]["number"]

    if resp_code== 600 and resp_message == "Transaction added successfully":
        print("\x1b[32mpass: {}\x1b[0m".format(transcation_number))
    else:
        print("\x1b[31mfail: {} code: {}, message:{}\x1b[0m".format(transcation_number,resp_code,resp_message))
    return resp_code,resp_message

if __name__ == "__main__":
    AddTransactionDetails()
