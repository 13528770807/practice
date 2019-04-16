import threading
import time

"""
# 多线程
def loop():
    print('thread name %s start ' % threading.current_thread().name)  # 子线程开始
    n = 0
    while n < 5:
        n += 1
        print('thread name %s ==== %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread name %s end' % threading.current_thread().name)  # 子线程结束


print('thread name %s start' % threading.current_thread().name)  # 主线程开始
t = threading.Thread(target=loop, name='loopName')
# t = threading.Thread(target=loop)
t.start()
t.join()
print('thread name %s end ' % threading.current_thread().name)  # 主线程结束
"""

# lock
balance = 0
lock = threading.Lock()


def change_it(n):
    print(threading.current_thread().name)
    global balance
    balance += n
    balance -= n


def run_thread(num):
    print(threading.current_thread().name)
    for i in range(10000):
        change_it(num)
        # 获取锁
        # lock.acquire()
        # try:
        #     change_it(num)
        # finally:
        #     # 释放锁
        #     lock.release()


print("main开始：", threading.current_thread().name)
t1 = threading.Thread(target=run_thread, args=(5,), name='loopName')
t2 = threading.Thread(target=run_thread, args=(8,))
t3 = threading.Thread(target=run_thread, args=(2,))
t4 = threading.Thread(target=run_thread, args=(6,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print("main结束", threading.current_thread().name)
print(balance)
