#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import logging


def delayed():
    logging.debug('worker running')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

# Timer 继承了 Thread 类，支持线程的延迟执行
# Timer 在延迟一段时间后启动工作，他可以在延迟的这段时间内任何时间点取消。
t1 = threading.Timer(0.3, delayed)
t1.setName('t1')
t2 = threading.Timer(0.3, delayed)
t2.setName('t2')

logging.debug('starting timers')
t1.start()
t2.start()

logging.debug('waiting before canceling %s', t2.getName())
time.sleep(0.2)
logging.debug('canceling %s', t2.getName())
# t2 线程实际上没有执行，设置了延迟 0.3 秒执行。在启动前被取消执行了
t2.cancel()
logging.debug('done')
