#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import requestTools
from Utilities.readexcel_xlsx import read_excel
from Utilities import APIlogs

logger = APIlogs.logs("LoyaltyReturnTransaction")


filename = "/pythonjulia/files/member_SR_TNF_1.xlsx"
sheetname = 'sheet1'

ws,ncol,nrow = read_excel(filename,sheetname)

def LoyaltyReturnTransaction():
    for i in range(2, nrow + 1):  # 行数
            till = ws.cell(row=i, column=1).value
            billing_time = ws.cell(row=i, column=2).value
            order_number = ws.cell(row=i, column=3).value
            SKU = ws.cell(row=i, column=4).value
            qty = ws.cell(row=i, column=5).value
            gross_amount = ws.cell(row=i, column=6).value
            amount = ws.cell(row=i, column=7).value
            discount = ws.cell(row=i, column=8).value
            rate = ws.cell(row=i, column=9).value
            mobile = ws.cell(row=i, column=10).value
            #print(till,billing_time,order_number,SKU,qty,gross_amount,amount,discount,rate)
            auth, header, preUrl = requestTools.requestPrepareWithDiffTill(till, "tnf_demo_md5", "Headers_MD5", "url_MD5")
            #print(auth, header, preUrl)
            # 接口的url
            url = preUrl+"v1.1/transaction/add?format=json"
            #print(url)
            bodyjson = {
                    "root":{
                        "transaction":{
                            "type": "return",
                            "return_type": "LINE_ITEM",
                            "billing_time":billing_time,
                            "number":order_number,
                            "gross_amount": gross_amount,
                            "amount":amount,
                            "customer":{"mobile":mobile},
                            "notes":"",
                            "line_items":{
                                "line_item":[
                                        {"item_code":SKU,
                                            "qty":qty,
                                            "rate":rate,
                                            "discount":discount,
                                            "value":gross_amount,
                                            "amount":amount,
                                            "serial":1,
                                            "description":"" }
            ]}}}}
            #print(bodyjson)
            logger.info(str(bodyjson))
            resp = requestTools.requestPOST(url,bodyjson, header, auth)
            #print(resp)
            if resp["response"]["status"]["code"] == 200:
                logger.info(str(resp))
            else: logger.info("[ISSUES]"+str(resp))
            logger.info("----------------------------------------------------------------------")


if __name__ == "__main__":
    LoyaltyReturnTransaction()
