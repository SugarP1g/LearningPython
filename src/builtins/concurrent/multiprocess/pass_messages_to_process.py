#!/usr/bin/env python
# encoding: utf-8

import multiprocessing


class MyClass(object):

    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print('Doing something fancy in {} for {}!'.format(
            proc_name, self.name))


def worker(q):
    obj = q.get()
    obj.do_something()


if __name__ == "__main__":

    # 可以使用Queue去实现进程间通信。
    # Queue是一个队列结构，实现 put / get 操作。
    # 任何可以序列化(pickle)的对象都可以通过Queue在进程间传递。
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()
    queue.put(MyClass("test"))

    queue.close()
    queue.join_thread()

    p.join()
