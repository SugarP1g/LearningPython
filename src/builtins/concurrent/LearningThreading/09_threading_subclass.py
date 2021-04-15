#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import logging


# 继承 Thread 类实现创建线程，覆写 run 函数中实现具体的逻辑
class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThread()
    t.start()
