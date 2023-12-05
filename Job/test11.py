# -*- coding:utf-8 -*-
import time

if __name__ == '__main__':
    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(now)
    print(now)-1