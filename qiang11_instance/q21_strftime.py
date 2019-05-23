import datetime
import time


# instance 1
now = int(time.time())
print(now)
timeArray = time.localtime(now)
print(timeArray)
otherStyletime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
print(otherStyletime)


# instance 2
now = datetime.datetime.now()
print(now)
otherStyletime2 = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyletime2)


# instance 3
timeStamp = 1558578033
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
print('dateArray:', dateArray)
otherStyletime3 = dateArray.strftime('%Y-%m-%d %H:%M:%S')
print(otherStyletime3)
