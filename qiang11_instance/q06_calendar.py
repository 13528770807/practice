import calendar

yy = int(input("请输入年份:"))
mm = int(input("请输入月份:"))

cale = calendar.month(yy, mm)  # 输出日历
print(cale)

cale1 = calendar.month(2019, 6)
print(cale1)

