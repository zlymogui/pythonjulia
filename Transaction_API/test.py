#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import requestTools
from Utilities.readexcel_xlsx import read_excel
from Utilities import APIlogs

#logger = APIlogs.logs("LoyaltyMixTransaction")
ws, ncol, nrow = read_excel("/pythonjulia/files/member_SR_TNF_Mix.xlsx", 'Sheet1')

def getTransactionLevelData():
    list = []
    for tn in range(2, nrow + 1):
        order_number1 = ws.cell(row=tn, column=3).value
        order_number2 = ws.cell(row=tn+1, column=3).value
        till = ws.cell(row=tn, column=1).value
        billing_time = ws.cell(row=tn, column=2).value
        mobile = ws.cell(row=tn, column=10).value
        tr_amount = ws.cell(row=tn, column=13).value
        tr_value = ws.cell(row=tn, column=14).value
        tr_discount = ws.cell(row=tn, column=15).value

        if order_number1 != order_number2:
            list1=[order_number1,till,billing_time,mobile,tr_amount,tr_value,tr_discount]
            list.append(list1)
    return list

def MergeLineItems():
    TrNums = getTransactionLevelData()
    for i in range(0, len(TrNums)):
        listItemJsonbody = []
        till = TrNums[i][1]
        billing_time = TrNums[i][2]
        mobile = TrNums[i][3]
        tr_amount = TrNums[i][4]
        tr_value = TrNums[i][5]
        tr_discount = TrNums[i][6]
        for j in range(2, nrow + 1):  # 行数
            #till = ws.cell(row=j, column=1).value
            #billing_time = ws.cell(row=j, column=2).value
            order_number = ws.cell(row=j, column=3).value
            SKU = ws.cell(row=j, column=4).value
            qty = ws.cell(row=j, column=5).value
            gross_amount = ws.cell(row=j, column=6).value
            amount = ws.cell(row=j, column=7).value
            discount = ws.cell(row=j, column=8).value
            rate = ws.cell(row=j, column=9).value
            #mobile = ws.cell(row=j, column=10).value
            transaction_type = ws.cell(row=j, column=11).value

            if order_number == TrNums[i][0]:
                    if transaction_type == 'SR':
                        jsonbodyR = {
                            "return_type": "LINE_ITEM",
                            "transaction_number": "",
                            "item_code": SKU,
                            "qty": qty,
                            "rate": rate,
                            "discount": discount,
                            "value": gross_amount,
                            "amount": amount,
                            #"serial": 1,
                            "notes": "",
                            "description": "",
                            "type": "return",
                            "purchase_time": "",
                            "attributes": ""}
                        listItemJsonbody.append(jsonbodyR)

                    elif transaction_type == 'SA':
                        jsonbodyA = {
                            "return_type": "",
                            "transaction_number": "",
                            "item_code": SKU,
                            "qty": qty,
                            "rate": rate,
                            "discount": discount,
                            "value": gross_amount,
                            "amount": amount,
                            #"serial": 2,
                            "notes": "",
                            "description": "",
                            "type": "",
                            "purchase_time": "",
                            "attributes": ""}
                        listItemJsonbody.append(jsonbodyA)
        #print(TrNums[i][1])
        #print(listItemJsonbody)
        #list.append([TrNums[i][0],listItemJsonbody])
        print(listItemJsonbody)
        print(len(listItemJsonbody))

        auth, header, preUrl = requestTools.requestPrepareWithDiffTill(till, "tnf_demo_md5", "Headers_MD5", "url_MD5")
        # 接口的url
        url = preUrl+"v1.1/transaction/add?format=json"
        bodyJson = 	{"root": {
                                "transaction": {
        	                            "type": "regular",
        	                            "return_type":"",
                                        "customer": {"mobile": mobile},
                                        "billing_time": billing_time,
                                        "purchase_time":"",
                                        "number": order_number,
                                        "amount": tr_amount,
                                        "discount":tr_discount,
                                        "gross_amount": tr_value,
                                        "line_items": {
                                                "line_item": listItemJsonbody }
                                }}}
        print(bodyJson)
        #logger.info(str(bodyJson))
        resp = requestTools.requestPOST(url,bodyJson, header, auth)
        print(resp)
        '''
        if resp["response"]["status"]["code"] == 200:
            logger.info(str(resp))
        else: logger.info("[ISSUES]"+str(resp))
        '''

MergeLineItems()



