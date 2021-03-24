#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eventlet
eventlet.monkey_patch()

import threading

print(eventlet.patcher.is_monkey_patched(threading.Thread))
