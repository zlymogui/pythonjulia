#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json

a = {'a1': None,'b1':None}
b = {
        "root":{
      "transaction":{
         "type":"not_interested_return",
         "return_type":"LINE_ITEM",
         "billing_time":"2015-2-1 16:18:41",#退货日期
         "purchase_time":"2001-1-1 16:18:41",#固定值
         "number":"T001",
         "amount":999,
         "gross_amount":999,
         "discount":0,
         "notes":"",
         "not_interested_reason":None,
         "line_items":{
            "line_item":[
               {
                  "return_type":"LINE_ITEM",
                  "item_code":"CGG374AXXL",
                  "description":"",
                  "qty":1,
                  "rate":999,
                  "discount":0,
                  "value":999,
                  "amount":999,
                  "serial":"1",
                  "notes":""
               }
            ]
         }
      }
   }
}

print(json.dumps(b))
