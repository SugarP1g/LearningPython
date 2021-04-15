#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def worker():
    # 获取当前线程的线程名
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'Exiting')


def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.3)
    print(threading.current_thread().getName(), 'Exiting')


# 通过关键字name指定线程名
t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
# 未命名，系统指定线程名。ex: Thread-1
w2 = threading.Thread(target=worker)  # 使用默认名字

w.start()
w2.start()
t.start()
