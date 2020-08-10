# 使用requests+多线程，并发10路，测试200次请求，统计百度首页的平均响应时间、最大响应时间、最小响应时间、请求成功率
# Author: TangYue
from concurrent.futures.thread import ThreadPoolExecutor
import requests


class UrlGet:
    pass


    # def __init__(self):
    #     self.thread_pool = ThreadPoolExecutor(3)

    def get_url(self):
        r = requests.get('https://www.baidu.com')
        s = r.status_code
        t = r.elapsed.total_seconds()
        print(f"response time is : {t}s")
        print(f"response code is : {s}")


if __name__ == '__main__':
    t = UrlGet()
    t.get_url()
