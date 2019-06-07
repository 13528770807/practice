

# 81,当字符串格式化书写的时候, 如果用户输入的有;+SQL语句,后面输入的SQL语句也会执行,
import json
import re

input_name = 'zq'
sql = "select * from demo where name=%s" % input_name
print('正常sql:', sql)

input_name2 = 'zq; drop datebase demo'
sql2 = 'select * from domo where name=%s' % input_name2
print('sql注入:', sql2)

# 解决方式, 通过参数传入的方式,解决sql注入
# input_name3 = 'zq'
# params = [input_name3]
# count = cs1.execute('select * from goods where name=%s', params)


# 82 s = "info:xiaoZhang 33 shandong" 用正则切分符输出 ['info', 'xiaoZhang', '33', 'shandong']
# 方法一
s = "info:xiaoZhang 33 shandong"
res = s.split(' ')  # ['info:xiaoZhang', '33', 'shandong']
str1 = ':'.join(res)  # info:xiaoZhang:33:shandong
li = str1.split(':')  # ['info', 'xiaoZhang', '33', 'shandong']
print(res)
print(str1)
print(li)

# 方法二
# | 表示根据冒号或空格切分
s1 = "info:xiaoZhang 33 shandong"
res1 = re.split(r':| ', s1)
print(res1)
print('*'*60)


# 83, 正则匹配以 163.com 结尾的邮箱
email_list = ['zhangsan@163.com', 'xiaowang@163.comheihei', '.com.lisi@qq.com']
for email in email_list:
    ret = re.match('[\w]{4,20}@163\.com$', email)
    if ret:
        print('aaa')
        print('以163.com结尾的:{},匹配结果为:{}'.format(email, ret.group()))  # ret.group() 把匹配到的字符提取出来
    else:
        print('不是以163.com结尾的:{}'.format(email))


# 84 递归求和 完成1+2+3+...+100
# 方法一 非递归
def sum1():
    j = 1
    num = 0
    while j <= 100:
        num += j
        j += 1
    return num


print(sum1())


# 方法二 递归
def get_sum(num2):
    if num2 >= 1:
        res2 = num2 + get_sum(num2-1)
    else:
        res2 = 0
    return res2


print(get_sum(100))


# 85, python 字典和 json 字典相互转换
# json.dumps() 将字典转成json字符串, json.loads() 将json字符串转成字典
dic = {'name': 'zhangsan', 'age': 18}
res2 = json.dumps(dic)
print(res2, type(res2))  # {"name": "zhangsan", "age": 18} <class 'str'>
ret = json.loads(res2)
print(ret, type(ret))  # {'name': 'zhangsan', 'age': 18} <class 'dict'>


# 86 MyISAM 与其innoDB 区别
"""
1、InnoDB 支持事务，MyISAM 不支持，这一点是非常之重要。事务是一种高
级的处理方式，如在一些列增删改中只要哪个出错还可以回滚还原，而 MyISAM
就不可以了；

2、MyISAM 适合查询以及插入为主的应用，InnoDB 适合频繁修改以及涉及到
安全性较高的应用；

3、InnoDB 支持外键，MyISAM 不支持；

4、对于自增长的字段，InnoDB 中必须包含只有该字段的索引，但是在 MyISAM
表中可以和其他字段一起建立联合索引；

5、清空整个表时，InnoDB 是一行一行的删除，效率非常慢。MyISAM 则会重
建表；
"""


# 87 统计字符串中某字符出现的次数
str2 = 'zhangsan lisi zhangsan wangwu'
res3 = str2.count('zhangsan')
print(res3)


# 88 字符转换大小写
str3 = 'MADE in China'
res4 = str3.upper()
print(res4)  # MADE IN CHINA
res5 = res4.lower()
print(res5)  # made in china


# 89 两种方式去空格
# 方法一
str4 = 'hello world ha ha'
res6 = str4.split(' ')
print(res6)   # ['hello', 'world', 'ha', 'ha']
res7 = ''.join(res6)
print(res7)  # helloworldhaha

# 方法二 re.replace()替换
res8 = str4.replace(' ', '')
print(res8)  # helloworldhaha


# 90 正则匹配不能以 4 和 7 结尾的手机号
tels = ["13528770807", "18329998402", "18802885279", "18888888887", "18866660004"]
for tel in tels:
    res9 = re.match("1\d{9}[0-3,5-6,8-9]", tel)
    if res9:
        print('不是以4和7结尾的:%s' % res9.group())
    else:
        print('是以4和7结尾的:%s' % tel)

