

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
print('='*60)


# 38、简述Django的orm
'''
ORM，全拼Object-Relation Mapping，意为对象-关系映射

实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，
而不需要修改代码只需要面向对象编程,orm操作本质上会根据对接的数据库引擎，
翻译成对应的sql语句,所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，
如果数据库迁移，只需要更换Django的数据库引擎即可
'''


# 39 [[1, 2], [3, 4], [5, 6]] 一行代吗得 [1, 2, 3, 4, 5, 6]
# 方法一
li3 = [[1, 2], [3, 4], [5, 6]]
new_li3 = []
for i in li3:
    for x in i:
        new_li3.append(x)

print(new_li3)

# 方法二
res = [x for i in li3 for x in i]
print(res)

# import numpy as np
# res1 = np.array(li3).flatten().tolist()
# print(res1)


# 40, x = "abc", y = "def", z = ["d", "e", "f"] 求 x.join(y), x.join(z)
x = "abc"
y = "def"
z = ["d", "e", "f"]
resu = x.join(y)  # join()括号中传入可遗代对象, x 做为参数传进去, os.path.join() 也经常用到
resu1 = x.join(z)
print(resu)  # dabceabcf
print(resu1)  # dabceabcf
