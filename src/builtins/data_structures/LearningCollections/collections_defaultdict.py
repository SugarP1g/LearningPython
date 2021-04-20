#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


def default_factory():
    return 'default value'


# 标准字典包含 setdefault() 方法，该方法用于检索值并在该值不存在时建立默认值。
# 相比之下，defaultdict允许调用方在初始化容器时预先指定默认值。
d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
# foo => bar
print('foo =>', d['foo'])
# bar这个key在字典中不存在，直接返回默认值。
# bar => default value
print('bar =>', d['bar'])
