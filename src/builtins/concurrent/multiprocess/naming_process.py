#!/usr/bin/env python
# encoding: utf-8

import multiprocessing
import time


def my_service():
    name = multiprocessing.current_process().name
    print(name, "Start.")
    time.sleep(2)
    print(name, "Exit.")


def worker():
    name = multiprocessing.current_process().name
    print(name, "Start.")
    time.sleep(3)
    print(name, "Exit.")


if __name__ == "__main__":
    service = multiprocessing.Process(name="my_service", target=my_service)
    worker_1 = multiprocessing.Process(name="worker-1", target=worker)
    worker_2 = multiprocessing.Process(target=worker)

    worker_1.start()
    worker_2.start()
    service.start()
