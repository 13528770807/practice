import os
from multiprocessing import Process

# p = os.fork()
# print('p:', p)
# if p == 0:
#     print('child id:%s, parent id: %s' % (os.getpid(), os.getppid()))
# else:
#     print('none')


def foo(name):
    print('%s currend id : %s' % (name, os.getpid()))


if __name__ == "__main__":
    print('主进程开始:%s' % os.getpid())
    pr = Process(target=foo, args=('test', ))
    print('子进程即将开始:%s' % os.getpid())
    pr.start()
    pr.join()
    print('子进程结束')



