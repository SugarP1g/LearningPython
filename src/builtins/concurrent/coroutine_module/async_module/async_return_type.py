#!/usr/bin/env python
# encoding: utf-8

async def test1():
    print("1")
    print("2")


async def test2():
    print("3")
    print("4")


def main1():
    # 调用函数test1、test2的时候，并没有进入函数体且执行函数内容，
    # 而是返回了一个coroutine（协程对象）。
    print(test2())
    print(test1())


def main2():
    # 执行结果如下：
    # Traceback (most recent call last):
    # 1
    # 2
    #   File "/Users/zer0ne/Documents/projects/LearningPython/src/builtins/concurrent/coroutine_module/async_module/async_return_type.py", line 30, in <module>
    #     main2()
    #   File "/Users/zer0ne/Documents/projects/LearningPython/src/builtins/concurrent/coroutine_module/async_module/async_return_type.py", line 24, in main2
    #     a.send(None)
    # StopIteration
    # sys:1: RuntimeWarning: coroutine 'test2' was never awaited

    # 程序先执行了test1协程函数，当test1执行完时报了StopIteration异常，这是协程函数执行完饭回的一个异常。
    # 我们可以用try except捕捉，来用判断协程函数是否执行完毕。
    a = test1()
    b = test2()
    a.send(None)
    b.send(None)


if __name__ == "__main__":
    # main1()
    main2()
