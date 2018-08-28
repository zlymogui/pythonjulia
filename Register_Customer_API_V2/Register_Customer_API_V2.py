#!/usr/bin/python
# -*- coding: UTF-8 -*-
# birthday,gender,city

import requests
import json
from Common import Headers
from Common import Urls

def RegisterWeChat(email,mobile,createDate,externalId,firstName,birthday,gender,openid,city): #*var_args_tuple不定长参数
        # 接口的url
        auth = (Headers.AUTHS["kolon_demo"]["Username"],Headers.AUTHS["kolon_demo"]["Password"])
        header = Headers.HEADERS1["Headers_MD5"]
        preUrl = Urls.URLS["url_MD5"]
        source = Urls.URLS["kolon_demo"]["Wechat"]["source"]
        accountId = Urls.URLS["kolon_demo"]["Wechat"]["accountId"]
        url = "%sv2/customers?source=%s&accountId=%s" % (preUrl, source, accountId)
        print(url)

        if birthday !='' and gender != '' and city != '' : # 111
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"fields\":{\"gender\":\"%s\",\"birthday\":\"%s\",\"city\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                       % (firstName, gender, birthday, city, openid, mobile, externalId, email, openid, mobile, createDate)
        elif birthday !='' and gender != ''and city == '': # 110
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"fields\":{\"birthday\":\"%s\",\"gender\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                       % (firstName, birthday,gender, openid, mobile, externalId, email, openid, mobile, createDate)
        elif birthday !='' and gender == ''and city == '': # 100
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"fields\":{\"birthday\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                       % (firstName, birthday, openid, mobile, externalId, email, openid, mobile, createDate)
        elif birthday =='' and gender != ''and city == '': # 010
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"fields\":{\"gender\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                       % (firstName, gender,openid, mobile, externalId, email, openid, mobile, createDate)
        elif birthday =='' and gender == ''and city != '': # 001
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"fields\":{\"city\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (firstName, city,openid, mobile, externalId, email, openid, mobile, createDate)
        elif birthday !='' and gender == ''and city != '': # 101
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"fields\":{\"birthday\":\"%s\",\"city\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (firstName, birthday,city,openid, mobile, externalId, email, openid, mobile, createDate)
        elif birthday =='' and gender != ''and city != '': # 011
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"fields\":{\"gender\":\"%s\",\"city\":\"%s\"},\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (firstName, gender,city,openid, mobile, externalId, email, openid, mobile, createDate)
        elif birthday =='' and gender == ''and city == '': # 000
                body = "{\"profiles\":[{\"firstName\":\"%s\",\"identifiers\":[{\"type\":\"wechat\",\"value\":\"%s\"},{\"type\":\"mobile\",\"value\":\"%s\"},{\"type\":\"externalId\",\"value\":\"%s\"},{\"type\":\"email\",\"value\":\"%s\"}],\"commChannels\":[{\"type\":\"wechat\",\"value\":\"%s\",\"primary\":true,\"verified\":true},{\"type\":\"mobile\",\"value\":\"%s\",\"primary\":true,\"verified\":true}]}],\"loyaltyInfo\":{\"loyaltyType\":\"loyalty\",\"attributionV2\": {\"createDate\": \"%s\"}}}" \
                   % (firstName,openid, mobile, externalId, email, openid, mobile, createDate)
        print(body)

        r = requests.request("post", url, data=body.encode('utf-8'), headers=header, auth=auth)
        #print(r)
        resp = json.loads(r.text)
        print(resp)
        if "createdId" in resp and "warnings" not in resp:
                userid = resp["createdId"]
                outputlist = [userid,'S1']
        elif "createdId" in resp and "warnings" in resp and "code" not in resp["warnings"]:
                userid = resp["createdId"]
                outputlist=[userid,'S2']
        elif "createdId" in resp and "warnings" in resp and "code" in resp["warnings"][0]:
                userid = resp["createdId"]
                code = resp["warnings"][0]["code"]
                status = resp["warnings"][0]["status"]
                message = resp["warnings"][0]["message"]
                outputlist = [userid,code, status, message,'S3']
        elif "createdId" not in resp and "errors" in resp and "code" in resp["errors"][0]:
                code = resp["errors"][0]["code"]
                status = resp["errors"][0]["status"]
                message = resp["errors"][0]["message"]
                outputlist = [code, status, message,'S4']
        elif "createdId" in resp and "errors" in resp and "code" in resp["errors"][0]:
                userid = resp["createdId"]
                code = resp["warnings"][0]["code"]
                status = resp["warnings"][0]["status"]
                message = resp["warnings"][0]["message"]
                outputlist = [userid, code, status, message,'S5']
        else:
                code = resp["errors"][0]["code"]
                status = resp["errors"][0]["status"]
                message = resp["errors"][0]["message"]
                outputlist=[code,status,message,'S6']
                #print(outputlist)
        print(outputlist)


email = 'jjjjjj2@123.com'
mobile = '18200000003'
createDate = '2018-07-08T17:53:00+08:00' # 2018/07/06 17:53
externalId = ''
firstName = 'o(╥﹏╥)o'
birthday = '1999-01-03' # 1999/01/02
gender = '男'
openid = 'juliaopenid18200000003'
city='上海'
RegisterWeChat(email,mobile,createDate,externalId,firstName,birthday,gender,openid,city)









