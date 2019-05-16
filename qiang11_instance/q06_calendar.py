import calendar

# yy = int(input("请输入年份:"))
# mm = int(input("请输入月份:"))
#
# cale = calendar.month(yy, mm)  # 输出日历
# print(cale)
import datetime

cale1 = calendar.month(2019, 6)  # 打印日历
print(cale1)


month_range = calendar.monthrange(2019, 6)  # 打印日历天数,返回元阻,第一参数(0-6)对应该星期几
print(month_range)


def getYesterday():
    '''获取昨天日期'''

    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


print(getYesterday())
