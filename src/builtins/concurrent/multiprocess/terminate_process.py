#!/usr/bin/env python
# encoding: utf-8

import multiprocessing
import time


def slow_worker():
    print('Starting worker')
    time.sleep(0.1)
    print('Finished worker')


if __name__ == "__main__":
    p = multiprocessing.Process(target=slow_worker)
    print('BEFORE:', p, p.is_alive())

    p.start()
    print('DURING:', p, p.is_alive())

    # 可以通过调用terminate函数去强制杀死子进程。
    # 主要是防止子进程hang住或者死锁了。
    # 执行可以发现，在调用terminate后，子进程已经退出。
    p.terminate()
    print('TERMINATED:', p, p.is_alive())

    p.join()
    print('JOINED:', p, p.is_alive())
