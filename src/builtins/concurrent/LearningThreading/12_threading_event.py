#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import threading
import time


def wait_for_event(e: threading.Event):
    """做任何事前先等待事件被设置。"""
    logging.debug('wait_for_event starting')
    # 一直等到Event被设置后再继续执行。
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)


def wait_for_event_timeout(e: threading.Event, t: int):
    """等待 t 秒。"""

    # 事件中的 is_set() 方法可以单独使用而不必担心阻塞住。
    while not e.is_set():
        logging.debug('wait_for_event_timeout starting')
        # wait() 方法可以接收一个参数，表示事件等待的超时时间。
        # 同时它返回一个布尔类型的对象，指代事件被设置了没有，所以我们可以根据它的返回来进行下一步行动。
        # 设置超时时间，最多等待 t 秒，如果 t 秒内，事件还是未被设置的话，则不再等待，继续执行。
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

# 每个 Event（事件）内部都有一个标记，我们可以用 set() 和 clear() 方法控制它。
# 其他线程可以使用 wait() 来暂停直到标记被设置才重新启动，使用这方法可以有效阻塞执行。
e = threading.Event()
t1 = threading.Thread(
    name='block',
    target=wait_for_event,
    args=(e,),
)
t1.start()

t2 = threading.Thread(
    name='nonblock',
    target=wait_for_event_timeout,
    args=(e, 2),
)
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(0.3)
e.set()
logging.debug('Event is set')
