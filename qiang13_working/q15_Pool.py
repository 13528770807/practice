import time
from multiprocessing.pool import Pool


def son(num):
    time.sleep(2)
    n = num+100
    print(n)
    return n


def Back(args):
    print('process over')


# 创建进和池 充许进程池同时放入3 个进程
pool = Pool(processes=3)

if __name__ == "__main__":
    for i in range(10):
        # 并行 callback 回调(主进程调用的)
        pool.apply_async(func=son, args=(i, ), callback=Back)

        # 并行
        # pool.apply_async(func=son, args=(i, ))

        # 串行
        # pool.apply(func=son, args=(i,))
    print('end')
    # 先关闭进程池再 jion
    pool.close()
    # 进程池中进程执行完毕再关闭, 如果注释,那么程序直接关闭
    pool.join()
