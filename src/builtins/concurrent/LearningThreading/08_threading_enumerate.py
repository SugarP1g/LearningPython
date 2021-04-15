#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import threading
import time
import logging


def worker():
    """thread worker function"""
    pause = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

# 获取当前进程主线程对象
main_thread = threading.main_thread()
# enumerate() 返回一个激活的 Thread 实例列表。
for t in threading.enumerate():
    # 这个列表包括当前线程，由于加入当前线程会导致死锁情况，所以应该跳过。
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()
