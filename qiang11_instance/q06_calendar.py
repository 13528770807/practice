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

    today = datetime.date.today()  # 今天
    oneday = datetime.timedelta(days=1)  # 一天
    yesterday = today - oneday
    return yesterday


Today = datetime.date.today()  # 今天
print(Today)
print(getYesterday())


# 方法二
def getYesterday2():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday


print(datetime.timedelta(-1))  # 负一天
print(getYesterday2())
