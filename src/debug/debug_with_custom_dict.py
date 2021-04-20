#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
遇到一个问题，字典的一个key的值被不知道的地方赋值了，导致在使用时报错类型错误。
解决的方法是实现了一个字典的子类，在赋值的魔法函数中增加打印堆栈，最终找到了修改的代码点。
"""


class CustomDict(dict):

    def __init__(self, seq=None, **kwargs):
        super(CustomDict, self).__init__(seq=seq, **kwargs)

    def __setitem__(self, key, value):
        import traceback
        print(traceback.format_stack())
        super(CustomDict, self).__setitem__(key, value)


if __name__ == "__main__":
    test = CustomDict()
    test["a"] = 'b'
    print(test["a"])
