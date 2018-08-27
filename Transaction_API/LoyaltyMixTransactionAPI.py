#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from Transaction_API import AddTransactionAPI2
from Utilities import datetimeformat
from Utilities import requestTools

def MixTransaction(preUrl,header,auth,user_id,billing_time,billing_time_add,order_number_mix, order_number_add):
    # 接口的url
    url = preUrl+"v1.1/transaction/add?format=json"
    print(url)
    bodyjson = 	{
    "root": {
        "transaction": {
        	"type": "regular",
        	"return_type":None,
            "customer": {
                "user_id": user_id
            },
            "billing_time": billing_time,
            "purchase_time":None,
            "number": order_number_mix,
            "amount": "300",
            "discount":200,
            "gross_amount": "500",
            "line_items": {
                "line_item": [
                    {
                    	"return_type": "LINE_ITEM",
                    	"transaction_number":order_number_add,
                        "item_code": "juliaxxxxxxxx01",
                        "qty": 1,
                        "rate": "500",
                        "discount": 50,
                        "value": "500",
                        "amount": "300",
						"serial":1,
						"notes":None,
						"description":"Goods|50;Points|100;Coupon|50;",
						"type":"return",
						"purchase_time":billing_time_add,
                        "attributes":None
                    },
                    {
                    	"return_type": None,
                    	"transaction_number":None,
                        "item_code": "juliaxxxxxxxx01",
                        "qty": 1,
                        "rate": "500",
                        "discount": 50,
                        "value": "500",
                        "amount": "300",
						"serial":2,
						"notes":None,
						"description":"Goods|50;Points|100;Coupon|50;",
						"type":None,
						"purchase_time":None,
                        "attributes":None}] },
            "payment_details": {
                "payment": [
                    {
                        "mode": "Exchange Lineitem",
                        "value": "300"
                    }]}}}}

    resp = requestTools.requestPOST(url, bodyjson, header, auth)
    print(resp)

if __name__ == "__main__":
    auth, header, preUrl = requestTools.requestPrepare("kolon_demo", "Headers_MD5", "url_MD5")
    print(auth, header, preUrl)
    order_number_add = requestTools.generateOrderNumber()
    billing_time_add = datetimeformat.getCurrentDateTime()
    AddTransactionAPI2.AddTransaction(auth, header, preUrl,'339915126', billing_time_add, order_number_add)

    order_number_mix = requestTools.generateOrderNumber()
    billing_time = datetimeformat.getCurrentDateTime()
    MixTransaction(auth, header, preUrl,'339915126', billing_time, billing_time_add, order_number_mix, order_number_add)
