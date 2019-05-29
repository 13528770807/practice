from multiprocessing import Pipe, Process


# https://www.jianshu.com/p/a4ac0c478be7
# 子进程函数 执行方法
def foo(subconn):
    print('from parent_conn:', subconn.recv())
    subconn.send('吃了的')


if __name__ == "__main__":
    # 创建管道两端
    parent_conn, child_conn = Pipe()

    # 创建子进程
    p = Process(target=foo, args=(child_conn, ))

    # 运行子进程
    p.start()

    # 进程间数据传递
    parent_conn.send('吃了么')
    print('from chile_conn:', parent_conn.recv())

    # 等待进程执行完后关闭
    p.join()