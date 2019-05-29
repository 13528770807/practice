import multiprocessing


# 创建子队列函数  子进程,内存独立,相当于数据传递
def foo(subQueue):
    subQueue.put('zhangsan')


if __name__ == "__main__":
    # 创建队列
    q = multiprocessing.Queue()

    # 创建进程对象
    p = multiprocessing.Process(target=foo, args=(q, ))

    # 开始进程
    p.start()

    # 获取队列中的资源
    print(q.get())