

# 41, try except else finally
import re

try:
    num = 100
except NameError as errorMsg:
    print('打印错误信息', errorMsg)
else:
    print('没有错误打印该信息')


try:
    num = 100
except NameError as errorMsg:
    print('打印错误信息', errorMsg)
finally:
    print('不管有没有错误都打印信息')


# 42, 变量值交换
a = 3
b = 6
# 方法一
# a, b = b, a
# 方法二
c = a
a = b
b = c
print(a, b)


# 43、举例说明zip（）函数用法
'''
zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。同时将这些序列中并排的元素配对。
zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数;当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组。
'''

li1 = [1, 2]
li2 = [3, 4]
tup1 = (1, 2)
tup2 = (3, 4)
str1 = 'zhang'
str2 = 'san'
res = [x for x in zip(li1, li2)]
res1 = [x for x in zip(tup1, tup2)]
res2 = [x for x in zip(str1, str2)]
print(res)
print(res1)
print(res2)


# 44, re.sub 正则替换
a = '张明 98 分'
res3 = re.sub(r'\d+', '100', a)
print(res3)
print('='*60)


# 45、写5条常用sql语句
'''
select * from table;
show tables;
show databases;
desc table;
delete from table where id=5;
update students set where gender=0, hometown='北京' where id=5;
'''


# 46、a="hello"和b="你好"编码成bytes类型
a = b'hello'
b = '你好'
byte_b = b.encode('utf8')
print(type(a))  # <class 'bytes'>
print(type(b))  # <class 'str'>
print(byte_b)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(type(byte_b))  # <class 'bytes'>


# 47, [1,2,3]+[4,5,6] 结果是多少
li3 = [1, 2, 3]
li4 = [4, 5, 6]
# li3.extend(li4)  #[1, 2, 3, 4, 5, 6]
li5 = li3+li4
print(li3)
print(li5)  # [1, 2, 3, 4, 5, 6]


# 48、提高python运行效率的方法
"""
1、使用生成器，因为可以节约大量内存
2、循环代码优化，避免过多重复代码的执行
3、核心模块用Cython  PyPy等，提高效率
4、多进程、多线程、协程
5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率
"""


# 49、简述mysql和redis区别
"""
redis： 内存型非关系数据库，数据保存在内存中，速度快
mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢
"""


# 50、遇到bug如何处理
"""
1、细节上的错误，通过print（）打印，能执行到print（）说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alert或console.log
2、如果涉及一些第三方框架，会去查官方文档或者一些技术博客。
3、对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会一条一条进行修改，
修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都会收藏做一些笔记记录。
4、导包问题、城市定位多音字造成的显示错误问题
"""
