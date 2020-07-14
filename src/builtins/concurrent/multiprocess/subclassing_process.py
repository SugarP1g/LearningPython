#!/usr/bin/env python
# encoding: utf-8

import multiprocessing


class Worker(multiprocessing.Process):

    def run(self):
        print('In {}'.format(self.name))
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        # 调用start函数时，实际上会调用Process.run函数。
        # 对run进程进行重写，可以改变进程创建的逻辑。
        p.start()
    for j in jobs:
        j.join()
