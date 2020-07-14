#!/usr/bin/env python
# encoding: utf-8

# 子进程退出状态如下表：
# ---------------------------------------------------------------------
# | Exit Code | Meaning                                               |
# |-----------|-------------------------------------------------------|
# | == 0      | no error was produced                                 |
# | > 0	      | the process had an error, and exited with that code   |
# | < 0	      | the process was killed with a signal of -1 * exitcode |
# |-----------|-------------------------------------------------------|

import multiprocessing
import sys
import time


def exit_error():
    sys.exit(1)


def exit_ok():
    return


def return_value():
    return 1


def raises():
    raise RuntimeError('There was an error!')


def terminated():
    time.sleep(3)


if __name__ == "__main__":
    jobs = []
    funcs = [exit_error, exit_ok, return_value, raises, terminated]

    for f in funcs:
        print('Starting process for', f.__name__)
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for j in jobs:
        j.join()
        # 调用exitcode可以看到子进程的退出状态：
        # 0: 表示正常执行结束退出
        # >0: 表示执行失败, exitcode为错误码
        # <0: 子进程被杀死
        print('{:>15}.exitcode = {}'.format(j.name, j.exitcode))
