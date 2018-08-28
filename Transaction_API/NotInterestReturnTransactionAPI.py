#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import requestTools
from Utilities.readexcel_xlsx import read_excel
from Utilities import APIlogs

logger = APIlogs.logs("NotInterestReturnTransactionTNF2")


filename = "/pythonjulia/files/nonmember_SR_TNF2.xlsx"
sheetname = 'sheet1'

ws,ncol,nrow = read_excel(filename,sheetname)

def NotInterestReturnTransaction():
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
            #print(till,billing_time,order_number,SKU,qty,gross_amount,amount,discount,rate)
            auth, header, preUrl = requestTools.requestPrepareWithDiffTill(till, "tnf_demo_md5", "Headers_MD5", "url_MD5")
            #print(auth, header, preUrl)
            # 接口的url
            url = preUrl+"v1.1/transaction/add?format=json"
            #print(url)
            bodyjson = {
                "root":{
                    "transaction":{
                        "type":"not_interested_return",
                        "return_type":"LINE_ITEM",
                        "billing_time":billing_time,#退货日期
                        "purchase_time":"2001-01-01 16:18:41",#固定值
                        "number":order_number,
                        "amount":amount,
                        "gross_amount":gross_amount,
                        "discount":discount,
                        "notes":"",
                        "not_interested_reason":"",
                        "line_items":{
                            "line_item":[
                                    {
                                        "return_type":"LINE_ITEM",
                                        "item_code":SKU,
                                        "description":"",
                                        "qty":qty,
                                        "rate":rate,
                                        "discount":discount,
                                        "value":gross_amount,
                                        "amount":amount,
                                        "serial":1,
                                        "notes":""
                                    }]
                        }}}}
            logger.info(str(bodyjson))
            resp = requestTools.requestPOST(url,bodyjson, header, auth)
            if resp["response"]["status"]["code"] == 200:
                logger.info(str(resp))
            else: logger.info("[ISSUES]"+str(resp))
            logger.info("----------------------------------------------------------------------")



if __name__ == "__main__":
    NotInterestReturnTransaction()
