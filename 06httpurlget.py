"""
Author: TangYue
"""
'''
使用requests+多线程，并发10路，测试200次请求，统计百度首页的平均响应时间、最大响应时间、最小响应时间、请求成功率
'''

import threading
from concurrent.futures.thread import ThreadPoolExecutor
import numpy
import requests


class UrlGet:
    global lis, lst
    lis, lst = [], []

    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(10)

    def magic_func(self):
        for i in range(200):
            self.thread_pool.submit(self.get_url, )

    def get_url(self):
        thread_name = threading.current_thread().name
        r = requests.get('https://www.baidu.com')
        s = r.status_code
        if s == 200:
            lst.append(1)
        t = r.elapsed.total_seconds()
        lis.append(t)

        print(f"response time is : {t}s")
        print(f"response code is : {s}")
        print(f"this is thread : {thread_name}")

    def calculiates(self):
        m = max(lis)
        n = min(lis)
        a = numpy.mean(lis)
        p = lst.count(1)
        print(f"max response time is : {m}s")
        print(f"min response time is : {n}s")
        print(f"avg response time is : {a}s")
        print(f"code200 percentage is : {p / 200 * 100}%")


if __name__ == '__main__':
    t = UrlGet()
    t.magic_func()
    t.thread_pool.shutdown()
    t.calculiates()
