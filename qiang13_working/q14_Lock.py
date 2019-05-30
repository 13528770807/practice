from multiprocessing import Process, Lock


# 子进程执行方法
def foo(num, lock):
    lock.acquire()
    print('zzzzz:', num)
    lock.release()


if __name__ == "__main__":
    lock = Lock()
    # 循环创建100个子进程
    for num in range(101):
        Process(target=foo, args=(num, lock)).start()
