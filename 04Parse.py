# 飞鸽传书
#    1、含有1w条url数据的文本文件（多线程构造）
#    2、解析url文件，获取里面参数值
#    3、将解析的参数值输出到文件中，输出格式为url\t参数\t\参数
# 要求
#    1、使用多进程实现
#    2、考虑到进程通信安全（进程锁）
# Author: TangYue
import string
from urllib.parse import urlparse
from multiprocessing import Pool, Lock


class Parse:
    pass

    def deal(self):
        ff = open("Url.txt", 'r')
        zz = open("Parse.txt", 'w')
        cc = open("Parse.txt", 'r')
        ii = open("Result.txt", 'w')
        lock = Lock()
        for eachline in ff.readlines():
            str = eachline.lstrip(string.digits)
            if str == '\n':
                str = str.strip('\n')
            lock.acquire()
            zz.write(str)
            lock.release()

        for eachline in cc.readlines():
            if len(eachline) < 150:
                str = eachline
            lock.acquire()
            zz.write(str)
            lock.release()

        for eachline in cc.readlines():
            result = urlparse(eachline)
            # 解析格式
            # ParseResult(scheme='https', netloc='www.test.com', path='/', params='',
            #             query='name=%E6%9D%8E%E5%A8%9C&sex=%E5%A5%B3&age=127&phone=13485666349',
            #             fragment='')
            query = result.query.split('&')
            combination = result.scheme.strip('') + '://' + result.netloc.strip('') + '/' + '\t' + \
                          query[0] + '\t' + query[1] + '\t' + query[2] + '\t' + query[3]
            lock.acquire()
            ii.write(combination)
            lock.release()


if __name__ == '__main__':
    test2 = Parse()
    test2.deal()

    pool = Pool(processes=3)

    for i in range(10000):
        pool.apply_async(func=test2.deal, args=(i,))

    pool.close()
    pool.join()

    print("end")
