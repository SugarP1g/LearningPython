#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


# logging是线程安全的
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

# 把某线程标记为守护线程，可以在构建时传入 daemon=True 或调用 set_daemon() 设置为 True
# 设置为守护线程，守护线程不会阻塞主线程退出。当主线程退出时，守护线程也会退出
d = threading.Thread(name='daemon', target=daemon, daemon=True)
# 默认情况下，线程是非守护的
# 非守护线程会阻塞主线程退出
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
