# -*- coding: UTF-8 -*-

# 21、列出python中可变数据类型和不可变数据类型，并简述原理
# 不可变数据类型：数值型、字符串型string和元组tuple
# 可变数据类型：列表list和字典dict
import re
from collections import Counter

from pip._vendor.progress import counter

a = 6
b = 6
print(id(a))  # 10919488
print(id(b))  # 10919488

li1 = [1, 2, 3]
li2 = [1, 2, 3]
print(id(li1))  # 140645676082312
print(id(li2))  # 140645615505288

li3 = [4, 5, 6]
print(id(li3))  # 140645615769864
li3.append(7)
print(id(li3))  # 140645615769864


# 22、去重
s = 'ajldjlajfdljfddd'
res = set(s)  # {'f', 'j', 'd', 'a', 'l'}
li = list(res)
li.sort(reverse=True)
print(li)  # ['l', 'j', 'f', 'd', 'a']
resl = ''.join(li)
print(resl)  # ljfda


# 23、lambda
sum1 = lambda x, y: x*y
print(sum1(8, 2))


# 24、字典键排序
dic = {'a': 9, 'c': 8, 'f': 2, 'b': 1}
li4 = sorted(dic.items(), key=lambda x: x[0])  # 键排序 [('a', 9), ('b', 1), ('c', 8), ('f', 2)]
li5 = sorted(dic.items(), key=lambda x: x[1])  # 值排序 [('b', 1), ('f', 2), ('c', 8), ('a', 9)]
new_li4 = {}
for i in li4:
    new_li4[i[0]] = i[1]

print(new_li4)  # {'a': 9, 'f': 2, 'b': 1, 'c': 8}


# 25、统计字符出现次数
# 方法一
str1 = 'abdddfbafsdbdsfsaffgbasio'
print(str1.count('a'))  # 4
set1 = set(str1)
print(set1)  # {'s', 'i', 'f', 'a', 'o', 'd', 'g', 'b'}
count_dic = {}
for i in set1:
    count_dic[i] = str1.count(i)

print(count_dic)  # {'s': 4, 'i': 1, 'o': 1, 'g': 1, 'f': 5, 'd': 5, 'a': 4, 'b': 4}


# 方法二
res2 = Counter(str1)
print(res2)  # Counter({'f': 5, 'd': 5, 's': 4, 'a': 4, 'b': 4, 'o': 1, 'i': 1, 'g': 1})
print('='*60)


# 26、正则
str2 = 'not 404 55.66 found 张三 99 深圳'
lis = str2.split(' ')
print('lis:', lis)  # lis: ['not', '404', '55.66', 'found', '张三', '99', '深圳']
res26 = re.findall(r'\d+\.?\d*|[a-zA-Z]+', str2)
print('res26:', res26)  # res26: ['not', '404', '55.66', 'found', '99']
for i in res26:
    if i in lis:
        lis.remove(i)

print(lis)  # ['张三', '深圳']
new_str = ' '.join(lis)
print(new_str)  # 张三 深圳
print('='*60)


# 27、求列表奇数
# 方法一
li6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_lst2 = []
for i in li6:
    if i % 2 != 0:
        new_lst2.append(i)

print(new_lst2)


# 方法二
def foo(lst):
    return lst % 2 != 0


new_lst = filter(foo, li6)
print(new_lst)  # 返回遗代器对象
new_lst = [x for x in new_lst]
print(new_lst)  # [1, 3, 5, 7, 9]
print('!'*60)


# 28、列表推导式 求奇数和
li7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res3 = [x for x in li7 if x % 2 != 0]
print(res3)  # [1, 3, 5, 7, 9]
print(sum(res3))  # 25


# 29、正则re.complie的作用
# re.compile将正则译成一个对象,加快速度,重复使用


# 30、数据类型
l = (1)
m = ("2")
n = (3,)
print(type(l))  # <class 'int'>
print(type(m))  # <class 'str'>
print(type(n))  # <class 'tuple'>

