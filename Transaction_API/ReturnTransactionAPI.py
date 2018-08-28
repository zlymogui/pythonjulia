#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import datetimeformat
from Utilities import requestTools
from Transaction_API.AddTransactionAPI2 import AddTransaction
import time

def ReturnTransaction(preUrl,header,auth,user_id,billing_time,order_number):
    # 接口的url
    url = preUrl+"v1.1/transaction/add?format=json"
    print(url)
    #Full_Return
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
    resp = requestTools.requestPOST(url, bodyjson, header, auth)
    print(resp)


if __name__ == "__main__":
    auth, header, preUrl = requestTools.requestPrepare("kolon_demo", "Headers_MD5", "url_MD5")
    billing_time = datetimeformat.getCurrentDateTime()
    orderNumber = requestTools.generateOrderNumber()
    AddTransaction(preUrl,header,auth,'339915126',billing_time,orderNumber)
    time.sleep(3)
    ReturnTransaction(preUrl,header, auth, '339915126',billing_time,orderNumber)
