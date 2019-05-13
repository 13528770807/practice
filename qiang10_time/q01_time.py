import datetime
import time

# 时间戳
time_stamp = time.time()
print(time_stamp)

# 时间戳转datetime
date_time = datetime.datetime.fromtimestamp(time_stamp)
print(date_time)

for i in range(10):
    pass
    # time.sleep(1)
    # print(time_str)

print('='*60)
today = datetime.date.today()  # 今天
print(today)

yesterday = today - datetime.timedelta(days=1)  # 昨天(如果days=2,代表前天)
print(yesterday)

last_month = today.month - 1 if today.month - 1 else 12  # 上个月
print(last_month)

# datetime 转时间戳
t = int(time.mktime(today.timetuple()))
print(t)

# datetime 转字符串
# today_str = today.strftime('%Y-%m-%d %H:%M:%S')
today_str = today.strftime('%Y-%m-%d')
print(today_str)

# 字符串转 datetime
today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
print(today)

# 补时差
today_time = today + datetime.timedelta(hours=8)
print('补时差：', date_time)
