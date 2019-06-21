import os
import random
import time
from multiprocessing import Queue, Process


def write(q):
    print('进程写入数据:%s' % os.getpid())
    li = ['A', 'B', 'C', 'D']
    for i in li:
        print('放入队列元素:', i)
        q.put(i)
        time.sleep(random.random())


def read(q):
    print('进程读取数据:%s' % os.getpid())
    while True:
        res = q.get(True)
        print('取出队表元素res:', res)


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('end--1---')
    pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止:
    print('end--2---')
