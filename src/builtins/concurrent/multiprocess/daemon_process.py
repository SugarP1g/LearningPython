#!/usr/bin/env python
# encoding: utf-8

import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


def main1():
    d = multiprocessing.Process(name="daemon_process", target=daemon)
    n = multiprocessing.Process(name="no_daemon_process", target=non_daemon)
    print("daemon_process default daemon value: %s" % d.daemon)
    print("no_daemon_process default daemon value: %s" % n.daemon)
    d.daemon = True
    n.daemon = False
    d.start()
    time.sleep(1)
    n.start()


def main2():
    d = multiprocessing.Process(name="daemon_process", target=daemon)
    n = multiprocessing.Process(name="no_daemon_process", target=non_daemon)
    print("daemon_process default daemon value: %s" % d.daemon)
    print("no_daemon_process default daemon value: %s" % n.daemon)
    d.daemon = True
    n.daemon = False
    d.start()
    time.sleep(1)
    n.start()
    # 阻塞父进程，直到子进程结束为止。
    # 从实验来看，子进程结束和join的先后顺序无关。
    # 唯一的限制是父进程需要等所有join的子进程结束后，才会继续向下执行。
    d.join()
    n.join()


def main3():
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True
    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False
    d.start()
    n.start()
    # join接受一个timeout的参数，意思就是如果超过了timeout的时间，不管子进程是否结束，join函数也会直接返回。
    d.join(1)
    # 可以看到子进程d仍然未结束，但是父进程已经继续执行了。
    print('d.is_alive()', d.is_alive())
    n.join()


if __name__ == "__main__":
    # main1()
    # main2()
    main3()
