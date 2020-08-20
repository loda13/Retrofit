# 飞鸽传书
#    1、含有1w条url数据的文本文件（多线程构造）
#    2、解析url文件，获取里面参数值
#    3、将解析的参数值输出到文件中，输出格式为url\t参数\t\参数
# 要求
#    1、使用多进程实现
#    2、考虑到进程通信安全（进程锁）
# Author: TangYue
import os
import random
import threading
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor  # 线程池
import faker


class Compile:
    pass

    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(11)

    def run(self):
        os.remove("Url.txt")
        for i in range(11):
            self.thread_pool.submit(self.main_logic, )

    def main_logic(self):
        ff = faker.Faker(locale='zh-CN')
        url = 'https://www.test.com/'
        thread_name = threading.current_thread().name
        threadLock = threading.Lock()
        for i in range(1000):
            parameter = {
                "name": ff.name_female(),
                "sex": "女",
                "age": random.randint(1, 133),
                "phone": ff.phone_number()
            }
            data = urlencode(parameter)
            threadLock.acquire()
            f = open("Url.txt", 'a')
            f.write(url + '?' + data)
            f.write('\n')
            f.close()
            threadLock.release()
            print(f"this is thread : {thread_name}")
            continue


if __name__ == '__main__':
    test1 = Compile()
    test1.run()
