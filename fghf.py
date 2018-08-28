#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

resp1 = {'createdId': 340189937}
resp2 = {'createdId': 340189937, 'warnings': []}
resp3 = {'createdId': 340189937, 'warnings': [{'status': False, 'code': 8051, 'message': 'Same Customer found in other sources,Merging with userId 340189937'}]}
resp4 = {'createdId': 340189937, 'errors': [{'status': False, 'code': 8051, 'message': 'Same Customer found in other sources,Merging with userId 340189937'}]}
resp5 = {'errors': [{'code': 8006, 'status': False, 'message': 'Add failed , Customer already exists for same  source'}]}

print("createdId" in resp1 and "warnings" not in resp1)
print("createdId" in resp2 and "warnings" in resp2 and "code" not in resp2["warnings"])
print("createdId" in resp3 and "warnings" in resp3 and "code" in resp3["warnings"][0])
print("createdId" in resp4 and "errors" in resp4 and "code" in resp4["errors"][0])
print("createdId" not in resp5 and "errors" in resp5 and "code" in resp5["errors"][0])

print(time.ctime(time.time()))