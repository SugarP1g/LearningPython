#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import logging


class MyThreadWithArgs(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        # 由于传入 Thread 构造函数的 args 和 kwargs 被保存在以 -- 开头的私有属性中，所以不能在子类中访问到。
        # 为了传入参数给自定义的线程类型，可以重新定义构造函数，把参数保存在能够在子类中看到的实例属性中。
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running with %s and %s',
                      self.args, self.kwargs)


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a': 'A', 'b': 'B'})
    t.start()
