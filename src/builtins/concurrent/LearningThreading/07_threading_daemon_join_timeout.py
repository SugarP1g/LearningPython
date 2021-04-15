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

# 默认情况下，join() 会无限期阻塞直到线程完成。
# 可以传递一个浮点数来表示阻塞的秒数。如果在超时时间内线程并未结束，join() 就会返回，不再继续等待。
d.join(0.1)
# 因为超时时间小于守护线程的睡眠时间，在 join() 返回后该线程仍然是 「存活」状态。
print('d.is_alive()', d.is_alive())
t.join()
