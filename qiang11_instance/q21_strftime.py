import datetime
import time


# instance 1
# 获得当前时间时间戳
now = int(time.time())
print(now)
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
print('timeArray:', timeArray)
otherStyletime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
print(otherStyletime)


# timeStamp = 1557502800
# timeArray = time.localtime(timeStamp)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(otherStyleTime)


# instance 2
# 获得当前时间
now = datetime.datetime.now()
print('now:', now)
# 转换为指定的格式
otherStyletime2 = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyletime2)


# instance 3
timeStamp = 1558578033
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
print('dateArray:', dateArray)
otherStyletime3 = dateArray.strftime('%Y-%m-%d %H:%M:%S')
print(otherStyletime3)
