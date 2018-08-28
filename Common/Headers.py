#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib

# 生成MD5
def generateMD5(str):
    # 创建MD5对象
    hl = hashlib.md5()

    # Tips
    # 此处必须声明encode
    # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
    hl.update(str.encode(encoding='utf-8'))

    #print('MD5加密前为 ：' + str)
    #print('MD5加密后为 ：' + hl.hexdigest())
    return hl.hexdigest()

# 生成SHA256
def generateSHA256(str):
    # 创建SHA256对象
    hl = hashlib.sha256()
    # Tips
    # 此处必须声明encode
    # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
    hl.update(str.encode(encoding='utf-8'))
    #print('SHA256加密前为 ：' + str)
    #print('SHA256加密后为 ：' + hl.hexdigest())
    return hl.hexdigest()


HEADERS = {
    "tnf_demo":{
         "Authorization":"Basic dG5mLmVjLmRlbW86NTFiNzQzNGE5ODQ3Y2ZmNGQ2N2IxYWY5MzIzMWNjZTcxYWE1MGJlNjgyNmQ4YjM3M2IyZWM2MGZiN2E1ZTA2OA==",
         "Accept":"application/json",
         "Content-Type": "application/json;charset=utf-8"},
    "tnf_demo_wechat":
        {"Authorization":"Basic dG5mLndlY2hhdC5kZW1vOjUxYjc0MzRhOTg0N2NmZjRkNjdiMWFmOTMyMzFjY2U3MWFhNTBiZTY4MjZkOGIzNzNiMmVjNjBmYjdhNWUwNjg=",
         "Accept":"application/json",
         "Content-Type": "application/json;charset=utf-8"},
    "tnf_live": {
        "Authorization": "Basic dG5mLmVjLmRlbW86NTFiNzQzNGE5ODQ3Y2ZmNGQ2N2IxYWY5MzIzMWNjZTcxYWE1MGJlNjgyNmQ4YjM3M2IyZWM2MGZiN2E1ZTA2OA==",
        "Accept": "application/json",
        "Content-Type": "application/json;charset=utf-8"},
    "tnf_live_import": {
        "Authorization": "Basic dG5mLmNoLmltcG9ydGxpdmU6NTFiNzQzNGE5ODQ3Y2ZmNGQ2N2IxYWY5MzIzMWNjZTcxYWE1MGJlNjgyNmQ4YjM3M2IyZWM2MGZiN2E1ZTA2OA==",
        "Accept": "application/json",
        "Content-Type": "application/json;charset=utf-8"},
    "purples": {
        "Authorization": "Basic cC53ZWNoYXQud2U6MTZkN2E0ZmNhNzQ0MmRkYTNhZDkzYzlhNzI2NTk3ZTQ=",
        "Accept": "application/json",
        "Content-Type": "application/json"},
    "descente_demo": {
        "Authorization": "Basic bDgwNzo5YjVlYzVmZGY0NTNiYzZkMjExZjlkM2U0MDc1NjYwOQ==",
        "Accept": "application/json",
        "Content-Type": "application/json"},
    "descente_live": {
        "Authorization": "Basic ZC5jaC50ZXN0OjliNWVjNWZkZjQ1M2JjNmQyMTFmOWQzZTQwNzU2NjA5",
        "Accept": "application/json",
        "Content-Type": "application/json"},
    "lee_demo": {
        "Authorization": "Basic bGVlLnRlc3Q6Y2MwM2U3NDdhNmFmYmJjYmY4YmU3NjY4YWNmZWJlZTU=",
        "Accept": "application/json",
        "Content-Type": "application/json"},
    "kolon_live": {
        "Authorization": "Basic a29sb24uY2gudGVzdGluZzpjZTI4NGQ2ZmY2ZjhjZWIxYWFjM2FkNjFiMTZmYjBmMw==",
        "Accept": "application/json",
        "Content-Type": "application/json"}
}

AUTHS = {
        "tnf_demo":{"Username":"tnf.ec.demo","Password":generateSHA256('tnf1234')},
        "tnf_demo_md5":{"Username":"tnf.ec.demo","Password":generateMD5('tnf1234')},
        "tnf_live":{"Username":"tnf.ch.admin","Password":generateSHA256('tnf1234')},
        "tnf_import_live":{"Username":"tnf.ch.importlive","Password":generateSHA256('tnf1234')},
        "kolon_live":{"Username":"kolon.ch.testing","Password":generateMD5('kolon123')},
        "kolon_demo":{"Username":"kolon.pos.demo","Password":generateMD5('kolon123')}
        }
#print(AUTHS)
#Auth = (Headers.AUTHS["tnf_demo"]["Username"],Headers.AUTHS["tnf_demo"]["Password"])
#r2 = requests.get(url,auth=Auth)

HEADERS1 = {
             "Headers_SHA256":{"Accept": "application/json","Content-Type": "application/json;charset=utf-8"},
             "Headers_MD5":{"Accept": "application/json","Content-Type": "application/json"}
            }