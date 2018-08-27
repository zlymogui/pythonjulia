# -*- coding:utf-8 -*-
import requests
from Common import Headers

url = "https://api.capillarytech.cn.com/v1.1/transaction/get?format=json&number=JULIA20180627001A"

#r1 = requests.get(url)
#print("未提供用户名密码：" + str(r1.status_code))

Auth = (Headers.AUTHS["tnf_demo"]["Username"],Headers.AUTHS["tnf_demo"]["Password"])
#Basic Authentication
r2 = requests.get(url,auth=Auth)
print("已提供用户名密码：" + str(r2.status_code))
print(r2.text)