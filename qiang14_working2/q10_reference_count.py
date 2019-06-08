import random
import re
import time


# 91, 简述python 引用计数机制
# python 的垃圾回收机制方要用到引用计数, 标记-清除为主分代清除为辅的机制,标记-清除和分代回收方要解决垃圾循环的难题

# 当使用del删除变量指向的对象时,如果引用计数不为1, 比如3, 那么它的引用记数为2, 再次调用del时,引用记数则减为1,
# 再用del时才真正删除对象
class Animal(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('调用__del__方法....')
        print('对象将被删除:%s' % self.name)


cat = Animal('四喜')
cat1 = cat
cat2 = cat1
print(id(cat), id(cat1), id(cat2))
print('正在删除cat.....')
del cat
print('正在删除cat1.....')
del cat1
print('正在删除cat2.....')
del cat2
print('程序2秒后结束')
# time.sleep(2)
print('*'*60)


# int("1.4"), int(1.4) 的结果?
# print(int("1.4"))  # ValuError
print(int(1.4))  # 1


# 93 列举3 条以上PEP8规范
# 列表, 元阻, 字典等 逗号后面空格
# 顶级定义空两行
# 类中方法与方法 之间空一格
# pycharm 条件判断缩进空4格
# 三引号进程注释


# 94 正则表达式匹配第一个URL
s = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_2016111131917_small.jpg" ' \
    'src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_small.jpg" style="display: inline">'

res = re.findall(r'https://.*?\.jpg', s)
print('第一个url:', res[0])
print('第二个url:', res[1])
res1 = re.search(r'https://.*?\.jpg', s)
print('search查找:', res1.group())


# 正则匹配中文
title = '你好, hello, 世界, 龙章大厦'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
res3 = pattern.findall(title)
print(res3)  # ['你好', '世界', '龙章大厦']


# 96 简述乐观锁和悲观锁
# 悲观锁, 它是数据被外界修改保持的态度, 依靠数据库提供的锁机制完成(对数据库性能开销大)
# 乐观锁, 基于数据版本记录机制实现


# 97 r,r+,rb,rb+ 文件打开模式的区别
"""
r: 读 指针-->文件开头
r+: 读写 指针-->文件开头
rb: 二进制 读 指针-->文件开头
rb+: 二进制 读写 指针-->文件开头
"""


# 98 Linux命令 重定向 > 和 >>
'''
> 覆盖
>> 追加
'''


# 99 正则表达式匹配出<html><h1>www.itcast.cn</h1></html>
labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
for label in labels:
    res4 = re.match(r'<(\w*)><(\w*)>.*</\2></\1>', label)
    if res4:
        print('是你想要的: %s' % res4.group())
    else:
        print('不是你想要的: %s' % label)


# 100 python 传参数是传值还是传地址
# 是引用传递, 对不可变类型(数字,字符串,元阻)不能引用对象的值, 对可变类型(列表,字典),可以修改引用对象的值
def selfAdd(a):
    a += a
    return a


num = 1
print(num)  # 1
print(selfAdd(num))  # 2
print(num)  # 1

li = [1, 2]
print(li)  # [1, 2]
print(selfAdd(li))  # [1, 2, 1, 2]
print(li)  # [1, 2, 1, 2]
print('*'*60)


# 101 求两个列表的交集, 并集, 差集
a = [1, 2, 3, 4]
b = [4, 3, 5, 6]
# 交集
res5 = [i for i in a if i in b]
print(res5)  # [3, 4]
print('intersection: ', list(set(a).intersection(set(b))))  # intersection:  [3, 4]

# 并集
for x in b:
    if x not in a:
        a.append(x)

print(a)  # [1, 2, 3, 4, 5, 6]
print('union: ', list(set(a).union(set(b))))  # union:  [1, 2, 3, 4, 5, 6]

# 差集
for i in b:
    if i in a:
        a.remove(i)

print(a)  # [1, 2]
print('difference: ', list(set(a).difference(set(b))))  # difference:  [1, 2]
print('*'*60)

# 102 生成0-100的随机数
print(100*random.random())  # 随机小数
print(random.randint(0, 100))   # 随机整数
print(random.choice(range(0, 101)))  # 随机整数


# 103 lambda 匿名函数的好处
# 精简代码, lambda 省去了定义函数, mpa 省去了 fro 循环的过程
lst = ['中国', '英国', '美国', "", '法国', "", '俄罗斯', 'hello', 'world']
print(list(map(lambda x: "空" if x == "" else x, lst)))
# ['中国', '英国', '美国', '空', '法国', '空', '俄罗斯', 'hello', 'world']
print('='*60)


# 104 常见的网络传输协议
# http udp tcp ftp smtp 等


# 105 单引号,双引号,三引号的用法
# 单引号,双引号一样, 可以嵌套使用, 单双分开, 不然要转义
# 三引号, 注释大段文字


# 106 python 垃圾回收机制
# 引用计数为主, 标记-删除和分代清除为辅的机制, 后者解决了循环引用的难题


# 107 http请求中get和post的区别
# 1, 数据传送方式, get:通过url, post: 放请求头中
# 2, 传送数据大小, get: 传送量小, post: 传送量大
# 3, 安全性:, get: 安全系数低, post: 安全系数高


# # 108 python 中读取excel文件的方法
# from pandas import pd
# res6 = pd.read_excel('excel_table.xlsx')
# print(res6)


# 109 多进程, 多线程
"""
进程:系统执行的基本单位, 相互独立, 稳定性好
线程:cpu 调度的基本单位, 也是线程的一部分, 共享资源
"""


# 110 python 正则中search 和 match
str1 = "小明年龄18岁 工资1800"
result = re.match('小明', str1)  # 匹配并提取开头数据, 没有匹配上抱错
print(result.group())  # 小明

result1 = re.search(r'\d+', str1)  # 匹配第一个并提取数据
print(result1.group())  # 18

result2 = re.findall(r'\d+', str1)  # 提取全部符合的数据
print(result2)  # ['18', '1800']


