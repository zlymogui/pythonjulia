#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import requestTools
from Utilities.readexcel_xlsx import read_excel
from Utilities import APIlogs

logger = APIlogs.logs("LoyaltyMixTransaction")
ws, ncol, nrow = read_excel("/pythonjulia/files/member_混合交易_round2_用于导入.xlsx", 'Sheet3')

def getTransactionLevelData():
    list = []
    for tn in range(2, nrow + 1):
        order_number1 = ws.cell(row=tn, column=3).value
        order_number2 = ws.cell(row=tn+1, column=3).value
        till = ws.cell(row=tn, column=1).value
        billing_time = ws.cell(row=tn, column=2).value
        mobile = ws.cell(row=tn, column=10).value
        tr_amount = abs(ws.cell(row=tn, column=13).value)
        tr_value = abs(ws.cell(row=tn, column=14).value)
        tr_discount = abs(ws.cell(row=tn, column=15).value)

        if order_number1 != order_number2:
            list1=[order_number1,till,billing_time,mobile,tr_amount,tr_value,tr_discount]
            list.append(list1)
    return list

def LoyaltyMixTransaction():
    TrNums = getTransactionLevelData()
    for i in range(0, len(TrNums)):
        listItemJsonbody = []
        orderNum = TrNums[i][0]
        till = TrNums[i][1]
        billing_time = TrNums[i][2]
        mobile = TrNums[i][3]
        tr_amount = TrNums[i][4]
        tr_value = TrNums[i][5]
        tr_discount = TrNums[i][6]
        for j in range(2, nrow + 1):  # 行数
            order_number = ws.cell(row=j, column=3).value
            SKU = ws.cell(row=j, column=4).value
            qty = abs(ws.cell(row=j, column=5).value)
            gross_amount = abs(ws.cell(row=j, column=6).value)
            amount = abs(ws.cell(row=j, column=7).value)
            discount = abs(ws.cell(row=j, column=8).value)
            rate = abs(ws.cell(row=j, column=9).value)
            transaction_type = ws.cell(row=j, column=11).value

            if order_number == orderNum:
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
                            "notes": "",
                            "description": "",
                            "type": "",
                            "purchase_time": "",
                            "attributes": ""}
                        listItemJsonbody.append(jsonbodyA)
        auth, header, preUrl = requestTools.requestPrepareWithDiffTill(till, "tnf_live", "Headers_SHA256", "url_SHA256")
        # 接口的url
        url = preUrl+"v1.1/transaction/add?format=json"
        bodyJson = 	{"root": {
                                "transaction": {
        	                            "type": "regular",
        	                            "return_type":"",
                                        "customer": {"mobile": mobile},
                                        "billing_time": billing_time,
                                        "purchase_time":"",
                                        "number": orderNum,
                                        "amount": tr_amount,
                                        "discount":tr_discount,
                                        "gross_amount": tr_value,
                                        "line_items": {
                                                "line_item": listItemJsonbody }
                                }}}
        #print(bodyJson)
        logger.info(str(bodyJson))
        resp = requestTools.requestPOST(url,bodyJson, header, auth)
        #print(resp)

        if resp["response"]["status"]["code"] == 200:
            logger.info(str(resp))
        else: logger.info("[ISSUES]"+str(resp))

if __name__ == "__main__":
    LoyaltyMixTransaction()



