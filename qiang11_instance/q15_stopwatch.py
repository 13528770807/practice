import time

while True:
    try:
        input('')
        print('开始')
        starttime = time.time()
        while True:
            print('计时', round(time.time()-starttime, 0), '秒')
            time.sleep(1)

    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('共计时间为:', round(endtime - starttime, 2), 'secs')
        break