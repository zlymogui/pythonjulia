#!/usr/bin/python
# -*- coding: UTF-8 -*-


from Utilities import datetimeformat
from Utilities import requestTools


def AddTransaction(preUrl,header,auth,user_id,billing_time,order_number):
    # 接口的url
    print(preUrl)
    url = preUrl + "v1.1/transaction/add?format=json"
    print(url)
    bodyjson = {
        "root": {
            "transaction": {
                "type": "regular",
                "notes": "",
                "customer": {
                    "user_id": user_id
                },
                "number": order_number,
                "billing_time": billing_time,
                "amount": "450",
                "discount": 550,
                "gross_amount": "1000",
                "line_items": {
                    "line_item": [
                        {
                            "item_code": "juliaxxxxxxxx01",
                            "qty": 1,
                            "rate": "500",
                            "discount": 50,
                            "value": "500",
                            "amount": "300",
                            "serial": 1,
                            "description": "Goods|50;Points|100;Coupon|50;"
                        },
                        {
                            "item_code": "juliaxxxxxxxx02",
                            "qty": 1,
                            "rate": "500",
                            "discount": 100,
                            "value": "500",
                            "amount": "150",
                            "serial": 1,
                            "description": "Goods|100;Points|200;Coupon|50;"
                        }
                    ]
                },
                "payment_details": {
                    "payment": [
                        {
                            "mode": "Cash",
                            "value": "450"
                        },
                        {
                            "mode": "Points",
                            "value": "300"
                        },
                        {
                            "mode": "Discount Coupon",
                            "value": "100"
                        }
                    ]
                }
            }
        }
    }
    resp = requestTools.requestPOST(url, bodyjson, header, auth)
    print(resp)

if __name__ == "__main__":
    auth, header, preUrl = requestTools.requestPrepare("kolon_demo", "Headers_MD5", "url_MD5")
    billing_time = datetimeformat.getCurrentDateTime()
    orderNumber = requestTools.generateOrderNumber()
    AddTransaction(preUrl,header, auth, '339915126',billing_time,orderNumber)
