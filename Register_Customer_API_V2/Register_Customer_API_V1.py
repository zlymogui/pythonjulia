#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Utilities import requestTools
from Utilities.readexcel_xlsx import read_excel
from Utilities.datetimeformat import string_toDate
#from Utilities.readexcel_xlsx import write_excel
from xlrd.timemachine import xrange

ws, ncol, nrow = read_excel("/pythonjulia/files/TNF会员数据_用于5.xlsx", '在系统中可以找到卡号')#

def RegisterCustomerV1():
    for i in range(2, nrow + 1):  # 行数
        mobile = ws.cell(row=i, column=6).value
        external_id = ws.cell(row=i, column=7).value
        first_name = ws.cell(row=i, column=5).value
        registered_on = ws.cell(row=i, column=3).value
        registered_on = registered_on[0:10]+" 08:00:00"  #因为现在intouch上会自动减掉8个小时，所以这边设置了加8个小时
        registered_till = ws.cell(row=i, column=4).value
        gender = ws.cell(row=i, column=2).value
        if gender == 'M':
            gender='男'
        else: gender = '女'
        birthday = ws.cell(row=i, column=1).value
        if birthday != None:
            birthday=birthday[0: 10]
        else: birthday = ""
        #print(registered_on,birthday)
        #print(mobile,external_id,first_name,registered_on,registered_till,gender,birthday)
        auth, header, preUrl = requestTools.requestPrepareWithDiffTill(registered_till, "tnf_live", "Headers_SHA256", "url_SHA256")
        print(auth, header, preUrl)
        # 接口的url
        url = preUrl+"v1.1/customer/add?format=json"
        bodyjson = {"root":{
                         "customer":[
                             {
                                "mobile":mobile,
                                "external_id":external_id,
                                "firstname":first_name,
                                "registered_on":registered_on,
                                "registered_till":registered_till,
                                "custom_fields":{
                                "field":[
                                    {
                                        "name":"gender",
                                        "value":gender
                                    },
                                   {
                                        "name":"birthday",
                                        "value":birthday
                                   }
                    ]}}]}}
        print(bodyjson)
        resp = requestTools.requestPOST(url, bodyjson, header, auth)
        print(resp)
        resp_code = resp["response"]["status"]["code"]
        if resp_code == 200:
            user_id = resp["response"]["customers"]["customer"][0]["user_id"]
            print(user_id)
            resplist = [user_id]
        else:
            print(resp)

if __name__ == "__main__":
    RegisterCustomerV1()
