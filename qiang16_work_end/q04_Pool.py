# *-* coding:utf8 *-*
import os
import random
import time
from multiprocessing import Pool


def foo(name):
    print('子进程%s开始:%s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    t = end - start
    print('子进程%s结束, 耗时:%.2f' % (name, t))


if __name__ == "__main__":
    p = Pool(2)
    for i in range(5):
        p.apply_async(foo, args=(i, ))
    print('等待子进程开始')
    p.close()
    p.join()
    print('子进程结束')
