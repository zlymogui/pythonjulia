#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Common import Headers
from Common import Urls

auth = (Headers.AUTHS["kolon_demo"]["Username"], Headers.AUTHS["kolon_demo"]["Password"])
header = Headers.HEADERS1["Headers_MD5"]
preUrl = Urls.URLS["url_MD5"]

def ReturnTransaction(user_id,billing_time,order_number):
    # 接口的url
    url = preUrl+"v1.1/transaction/add?format=json"
    print(url)
    bodyjson = { "root": {
                "transaction": [{
                        "type": "return",
                        "return_type": "LINE_ITEM",
                        "number": order_number,
                        "amount": "450",
                        "billing_time": billing_time,
                        "notes": "",
                        "customer": {"user_id": user_id},
                        "line_items": {
                            "line_item": [
                                {"item_code": "juliaxxxxxxxx01",
                                "qty": 1,
                                "rate": "500",
                                "discount": 50,
                                "value": "500",
                                "amount": "300",
						        "serial":1,
						        "description":"Goods|50;Points|100;Coupon|50;"},
                                {"item_code": "juliaxxxxxxxx02",
                                    "qty": 1,
                                    "rate": "500",
                                    "discount": 100,
                                    "value": "500",
                                    "amount": "150",
						            "serial":1,
						            "description":"Goods|100;Points|200;Coupon|50;"}]}}]}}
    body=json.dumps(bodyjson,ensure_ascii=False)
    r = requests.request("post", url, data=body, headers=header, auth=auth)
    resp = json.loads(r.text)
    print(resp)


if __name__ == "__main__":
    ReturnTransaction('339915126','2018-07-09 10:18:22','JULIA20180709001')
