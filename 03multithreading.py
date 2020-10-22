"""
Author: TangYue
"""
'''
多线程实现数字相减，从100减到0
使用多线程
使用线程锁，保证多线程运行输出结果正常

'''

from concurrent.futures import ThreadPoolExecutor  # 线程池
import time
import threading


class Operation:
    pass

    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(3)

    def main_logic(self):
        global i
        i = 100
        threadLock = threading.Lock()
        while i > 0:
            if i > 0:
                threadLock.acquire()
                i -= 1
                threadLock.release()
                self.thread_pool.submit(self.subtraction, i)
            else:
                break

    def subtraction(self, result):
        thread_name = threading.current_thread().name
        print(f'线程名称 : {thread_name}')
        print(f'result : {result}')
        time.sleep(1)


if __name__ == "__main__":
    test = Operation()
    test.main_logic()
