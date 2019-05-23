import datetime
import time


# instance 1
# 先获得时间数组格式的日期
threeDaysAgo = datetime.datetime.now() - datetime.timedelta(days=3)
print(threeDaysAgo)

# 转换为时间戳
timeStamp = time.mktime(threeDaysAgo.timetuple())
print(timeStamp)

# 转换为其他字符串格式
otherStyleTime = threeDaysAgo.strftime('%Y-%m-%d %H:%M:%S')
print(otherStyleTime)


# instance 2
#给定时间戳
timeStamp2 = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp2)
print('dateArray:', dateArray)

otherStyleTime2 = dateArray - datetime.timedelta(days=3)
print(otherStyleTime2)
