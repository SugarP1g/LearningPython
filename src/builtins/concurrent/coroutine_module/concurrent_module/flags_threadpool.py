#!/usr/bin/env python
# encoding: utf-8

import time

from concurrent import futures

import requests

MAX_WORKERS = 20

url_list = [
    "http://www.baidu.com",
    "http://www.taobao.com",
    "http://www.jd.com",
    "http://www.hao123.com"
]

workers = min(MAX_WORKERS, len(url_list))


def download(url):
    resp = requests.get(url)
    print(resp.status_code)
    return resp.status_code


start_time = time.time()

with futures.ThreadPoolExecutor(workers) as executor:
    result_list = executor.map(download, sorted(url_list))

    for result in result_list:
        print("result is: ", result)

print("Consume %.3f second." % float(time.time() - start_time))
