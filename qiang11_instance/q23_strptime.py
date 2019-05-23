import time


a1 = "2019-5-10 23:40:00"
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")
print(timeArray)
print(type(timeArray))


timeStamp = int(time.mktime(timeArray))
print(timeStamp)


# # 格式转换 - 转为 /
# a2 = "2019/5/10 23:40:00"
# # 先转换为时间数组,然后转换为其他格式
# timeArray2 = time.strptime(a2, "%Y-%m-%d %H:%M:%S")
# print(timeArray2)
# otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
# print(otherStyleTime)