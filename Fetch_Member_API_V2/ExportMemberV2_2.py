#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities.requestTools import requestGET,requestPrepareWithDiffTill
from Utilities.readexcel_xlsx import read_excel
from Utilities.writeexcel_xlsx import write_excel

filename = '/pythonjulia/files/微信--需要手机号和卡号_2.xlsx'
sheet = 'Sheet1'
ws, ncol, nrow = read_excel(filename, sheet)

def ExportMemberV2_2Details():
    for i in range(2, nrow + 1):  # 行数
        userId = ws.cell(row=i, column=4).value
        #print(userId)
        auth, header, preUrl = requestPrepareWithDiffTill("tnf.ch.wechatlive","tnf_live", "Headers_SHA256","url_SHA256")
        #print(auth, header, preUrl)
        # 接口的url
        url = "%sv2/customers/%s?source=ALL&embed=points" % (preUrl,userId)
        print(url)
        resp = requestGET(url,header,auth)
        resp_mobile = ''
        resp_externalId=''
        if len(resp["profiles"])>=2:
            for num in range(0,len(resp["profiles"])):
                if resp["profiles"][num]["source"] =="WECHAT":
                    accountId = resp["profiles"][num]["accountId"]
                    for r in resp["profiles"][num]["identifiers"]:
                        if r["type"] == "mobile":
                            resp_mobile = r["value"]
                        if r["type"] == "externalId":
                            resp_externalId = r["value"]
                    resplist = [resp_mobile, resp_externalId, userId,accountId]
                    print("->=2--")
                    write_excel(filename, sheet, i, resplist[0], resplist[1], resplist[2],accountId)
        elif len(resp["profiles"])==1:
            accountId = resp["profiles"][0]["accountId"]
            for r in resp["profiles"][0]["identifiers"]:
                if r["type"]=="mobile":
                    resp_mobile = r["value"]
                if r["type"] == "externalId":
                     resp_externalId = r["value"]
            resplist = [resp_mobile,resp_externalId,userId,accountId]
            print("-==1--")
            write_excel(filename,sheet,i,resplist[0],resplist[1],resplist[2],accountId)
        else: write_excel(filename,sheet,i,"no profile","no profile","no profile")

ExportMemberV2_2Details()