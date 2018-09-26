#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import requestTools
from Utilities.readexcel_xlsx import read_excel
from Utilities import APIlogs
from Utilities.writeexcel_xlsx import write_excel

filename = '/pythonjulia/files/TMALL会员_用于导入demo.xlsx'
sheetname = '积分情况'
logger = APIlogs.logs("V2TMALLRegister")
ws, ncol, nrow = read_excel(filename, sheetname)

def RegisterCustomerV2TMALL():
    for i in range(2, nrow + 1):  # 行数
        mobile = ws.cell(row=i, column=1).value
        externalId = ws.cell(row=i, column=6).value
        firstname = ws.cell(row=i, column=2).value
        joint_date = ws.cell(row=i, column=5).value
        joint_date = str(joint_date)[0:10]+"T00:00:00+08:00"
        registered_till = ws.cell(row=i, column=4).value
        birthday = ws.cell(row=i, column=3).value
        if birthday != None:
            birthday=str(birthday)[0:10]
        else: birthday = ""
        #print(registered_on,birthday)
        #print(mobile,external_id,first_name,registered_on,registered_till,gender,birthday)
        auth, header, preUrl = requestTools.requestPrepareWithDiffTill(registered_till, "tnf_demo", "Headers_SHA256", "url_SHA256")
        print(auth, header, preUrl)
        # 接口的url
        url = preUrl+"v2/customers?source=TMALL&accountId=928417138"
        bodyjson = {
                        "profiles": [
                                {
                                    "firstName": firstname,
                                    "fields": {
                                        "birthday": birthday
                                },
                        "identifiers": [
                                {
                                    "type": "mobile",
                                    "value": mobile
                                },
				                {
                                    "type": "externalId",
                                    "value": externalId
                                }
                                ],
                        "commChannels": [
                            {
                                "type": "mobile",
                                "value": mobile,
                                "primary": "true",
                                "verified": "true"
                            }
                        ]
                     }
                ],
            "loyaltyInfo": {
            "loyaltyType": "loyalty",
		    "attributionV2":{
                    "createDate":joint_date}}}

        logger.info(str(bodyjson))
        resp = requestTools.requestPOST(url, bodyjson, header, auth)
        logger.info(str(resp))
        userid = ''
        if "createdId" in resp and "warnings" not in resp:
            userid = resp["createdId"]
            outputlist = [userid, 'S1']
        elif "createdId" in resp and "warnings" in resp and "code" not in resp["warnings"]:
            userid = resp["createdId"]
            outputlist = [userid, 'S2']
        elif "createdId" in resp and "warnings" in resp and "code" in resp["warnings"][0]:
            userid = resp["createdId"]
            code = resp["warnings"][0]["code"]
            status = resp["warnings"][0]["status"]
            message = resp["warnings"][0]["message"]
            outputlist = [userid, code, status, message, 'S3']
        elif "createdId" not in resp and "errors" in resp and "code" in resp["errors"][0]:
            code = resp["errors"][0]["code"]
            status = resp["errors"][0]["status"]
            message = resp["errors"][0]["message"]
            outputlist = [code, status, message, 'S4']
        elif "createdId" in resp and "errors" in resp and "code" in resp["errors"][0]:
            userid = resp["createdId"]
            code = resp["warnings"][0]["code"]
            status = resp["warnings"][0]["status"]
            message = resp["warnings"][0]["message"]
            outputlist = [userid, code, status, message, 'S5']
        else:
            code = resp["errors"][0]["code"]
            status = resp["errors"][0]["status"]
            message = resp["errors"][0]["message"]
            outputlist = [code, status, message, 'S6']

        if userid in outputlist:
            write_excel(filename,sheetname,i,7,str(userid))
            write_excel(filename, sheetname,i,8,str(outputlist))
        else: write_excel(filename,sheetname,i,8,str(outputlist))

        logger.info(str(outputlist))
        logger.info("------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    RegisterCustomerV2TMALL()
