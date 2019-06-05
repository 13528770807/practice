

# 31,合并列表
import datetime
import re

li1 = [1, 2, 3, 4, 5, 6]
li2 = [4, 5, 6, 7, 8, 9]
li1.extend(li2)  # [1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9]
print(li1)
li1.sort(reverse=False)
print(li1)  # [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9]


'''32、用python删除文件和用linux命令删除文件方法
python：os.remove(文件名)
linux:       rm  文件名
'''


# 32,打印时间截
now = datetime.datetime.now()
print(now)
str_time = now.strftime('%Y-%m-%d %H:%M:%S')
print('datetime:', str_time)  # datetime: 2019-06-05 17:29:01
week_day = datetime.datetime.now().isoweekday()
print('星期:', week_day)  # 星期: 3
print('@'*60)


# 34,数据库优化查询方法
# 外键,索引,联合查询,选择特定字段等


# 35,绘图工具
# pychart, matplotlib


# 36, 自定义异常
def foo():
    try:
        for i in range(5):
            if i > 3:
                raise Exception('i > 3 le')
    except Exception as e:
        print(e)


foo()


#  37、正则表达式匹配中，（.*）和（.*?）匹配区别？
# （.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
# （.*?）是非贪婪匹配，会把满足正则的尽可能少匹配

s = '<a>hehe</a><a>haha</a>'
s1 = re.findall('<a>(.*)</a>', s)
s2 = re.findall('<a>(.*?)</a>', s)
print(s1)  # ['hehe</a><a>haha']
print(s2)  # ['hehe', 'haha']


# 38、简述Django的orm

