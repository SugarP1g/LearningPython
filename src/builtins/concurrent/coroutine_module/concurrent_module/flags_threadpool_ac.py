#!/usr/bin/env python
# encoding: utf-8


from concurrent import futures

from flags_threadpool import download
from flags_threadpool import url_list


def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download, cc)

            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        # as_completed 函数的参数是一个Future对象列表，返回值是一个迭代器，在期物运行结束后产出期物。
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


print(download_many(url_list))