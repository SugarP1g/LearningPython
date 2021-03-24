#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eventlet

eventlet.monkey_patch()

import multiprocessing
import threading
import time


class AuditProcess(object):
    shared_msg_lock = multiprocessing.Lock()

    # MAX_QUEUE_LENGTH与审计规模有关，为3n的数量级,multiprocessing队列超过1048会挂起
    # 分别为data_collect progress，data_audit progress和audit_result
    # 其中progress为字符串，audit_result为列表
    # 队列长度如果超过最大长度，表示子进程出现异常
    # 通过put_nowait可以抛出Full异常
    MAX_QUEUE_LENGTH = 1048
    async_info_queue = multiprocessing.Queue(MAX_QUEUE_LENGTH)


def child_do_it(param):
    print("this is child do it.")
    eventlet.sleep(3)
    print("param: " + param)
    AuditProcess.async_info_queue.put_nowait(str(param))


def parent_do_it(proc_obj: multiprocessing.Process):
    print("this is parent do it.")
    eventlet.sleep(1)
    proc_obj.join(timeout=int(10))

    print(AuditProcess.async_info_queue.get_nowait())

    if proc_obj.is_alive():
        print("child proc is alive")
    else:
        print("child proc is not alive")

    AuditProcess.shared_msg_lock.release()
    print("this is parent do it end.")


def main():
    AuditProcess.shared_msg_lock.acquire()
    param = "just a test param."
    p = multiprocessing.Process(target=child_do_it, args=(param,))
    p.daemon = True
    p.start()

    t = threading.Thread(target=parent_do_it, args=(p,))
    t.start()

    print("this is main end.")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
