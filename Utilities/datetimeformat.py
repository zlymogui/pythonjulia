#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from datetime import datetime, timedelta

#把字符串转成datetime
def string_toDatetime(string):  #  string格式"2016/09/18 12:51"
    string = string+":00"
    a = time.strptime(string, "%Y/%m/%d %H:%M:%S")
    b = time.strftime("%Y-%m-%dT%H:%M:%S+08:00", a)
    print(b)
    return b

#把字符串转成date
def string_toDate(string): # string格式'1992/02/18'
    a = time.strptime(string, "%Y/%m/%d")
    b = time.strftime("%Y-%m-%d", a)
    print(b)
    return b

def dateTimeHelper():
    _rnow = datetime.now()
    _now = _rnow.strftime('%Y-%m-%d %H:%M:%S')
    _now_fiel = _rnow.strftime('%Y-%m-%d-%H')
    _yesterday = _rnow - timedelta(days=1)
    _yesterdaymin = _yesterday.strftime('%Y-%m-%d 00:00:00')
    _yesterdaymax = _yesterday.strftime('%Y-%m-%d 23:59:59')

def getCurrentDateTime():
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    CurrentDateTime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
    return CurrentDateTime

def getCurrentDateTimef1():
    ISOTIMEFORMAT = '%Y%m%d%H%M%S'
    CurrentDateTime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
    return CurrentDateTime

