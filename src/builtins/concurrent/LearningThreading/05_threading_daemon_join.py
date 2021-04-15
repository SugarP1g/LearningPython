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


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# 如果要等待标记为守护的线程结束，可以使用 join() 方法
# 使用 join() 后，守护线程就有机会执行完成并打印出 "Exiting"
d.join()
t.join()
