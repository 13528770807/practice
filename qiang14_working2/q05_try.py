

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


# 48、提高python运行效率的方法 todo

