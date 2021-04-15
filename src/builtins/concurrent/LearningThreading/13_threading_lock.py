#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import random
import threading
import time


# 除了同步多个线程的操作，控制共享资源的访问以防止污染或丢失数据也是非常重要的。
# Python 的内置数据结构（列表（list），字典（dict）等....）都是线程安全的，有「原子操作」的对象都是这样。
# （全局解释器锁会保护这样的 Python 内部数据结构在更新时线程不会被释放）。
# 其他 Python 的数据结构或者说较简单的类型如整数浮点数则不会受此保护。我们可以使用 Lock 对象来保护某对象的访问。

class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)
