import threading
import time


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


