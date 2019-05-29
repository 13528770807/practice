import multiprocessing
import time


# 子进程执行方法
def foo(n):
    time.sleep(2)
    print(n)


# 循环创建 10 个进程
for i in range(10):
    print('i ===>', i)
    # 创建子进程实例
    p = multiprocessing.Process(target=foo, args=('person: %s' % i,))
    # 运行子进程
    p.start()