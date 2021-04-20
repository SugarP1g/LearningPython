#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eventlet

eventlet.patcher.monkey_patch(socket=True, time=True)

import threading
import time


class Leak(threading.Thread):
    def __init__(self):
        super(Leak, self).__init__()

    def run(self):
        # 文件句柄泄露
        # The leaking anon_inode is created by pool.join(), which has a time.sleep in it.
        # Before patching, it use system call select to implement sleep, while gevent use epoll to implement sleep.
        # Gevent (libev) create a epoll fd for each thread if there isn't a epoll fd (aka anon_inode),
        # but never close the fd even the thread exits, thats why we met the anon_inode leak issue.
        time.sleep(1)


threads = []
for _ in range(5):
    t = Leak()
    threads.append(t)

raw_input()
for t in threads:
    t.start()
raw_input()
