import calendar

# year = int(input('请输入年份:'))
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('{}为闰年'.format(year))
# else:
#     print('{}不是闰年'.format(year))


def calendar_data(year):
    if calendar.isleap(year):
        print('{}为闰年'.format(year))
    else:
        print('{}不是闰年'.format(year))


calendar_data(2000)
calendar_data(1999)
