

# 71, sort(), sorted()
import random

lis = [2, 6, 5, -1, 8, -9]
# lis.sort()  # sort没有返回值
# print(lis)  # [-9, -1, 2, 5, 6, 8]

print(sorted(lis, key=lambda x: x))  # [-9, -1, 2, 5, 6, 8]


# 72 lambda()
foo = [1, 9, -2, 4, 7, -8, 5]
print(sorted(foo, key=lambda x: x))  # [-8, -2, 1, 4, 5, 7, 9]


# 73 lambda() 正数小到大,负数大到小
foo1 = [1, 9, -2, 4, 7, -8, 5]
print(sorted(foo1, key=lambda x: (x < 0, abs(x))))  # [1, 4, 5, 7, 9, -2, -8]


# 74列表嵌套字典排age排序
foo2 = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 19}, {'name': 'wuangwu', 'age': 16}]
print(sorted(foo2, key=lambda x: x['age']))
# [{'name': 'wuangwu', 'age': 16}, {'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 19}]


# 75 列表嵌套元阻分别按数字和字母排序
foo2 = [('zs', 39), ('si', 80), ('ww', 62), ('zl', 90)]
print(sorted(foo2, key=lambda x: x[0]))  # [('si', 80), ('ww', 62), ('zl', 90), ('zs', 39)]
print(sorted(foo2, key=lambda x: x[1]))  # [('zs', 39), ('ww', 62), ('si', 80), ('zl', 90)]


# 76 列表嵌套列表排序,数字相同按字母排序
foo3 = [['gz', 82], ['xg', 17], ['hn', 17], ['hz', 18]]
print(sorted(foo3, key=lambda x: (x[1], x[0])))  # [['hn', 17], ['xg', 17], ['hz', 18], ['gz', 82]]


# 77 根据键对字典排序
# method 1
foo4 = {'zs': 11, 'ls': 28, 'ww': 19, 'zl': 22}
res = sorted(foo4.items(), key=lambda x: x[0])
print('res:', res)  # res: [('ls', 28), ('ww', 19), ('zl', 22), ('zs', 11)]
res1 = {x[0]: x[1] for x in res}  # 字典推导式
print(res1)  # {'ww': 19, 'ls': 28, 'zl': 22, 'zs': 11}
print('='*60)


# 78 method 2  zip()
res2 = zip(foo4.keys(), foo4.values())
print(res2)  # <zip object at 0x7fd45e5df5c8>
li = [i for i in res2]
print(li)  # [('ww', 19), ('zl', 22), ('zs', 11), ('ls', 28)]
res3 = sorted(li, key=lambda x: x[0])
print(res3)  # [('ls', 28), ('ww', 19), ('zl', 22), ('zs', 11)]
dic = {i[0]: i[1] for i in res3}
print(dic)  # {'ww': 19, 'zs': 11, 'zl': 22, 'ls': 28}
print('*'*60)


# 79 字典推导式, 列表推导式, 生成器
dic = {k: random.randint(8, 12) for k in ['a', 'b', 'c', 'd']}  # 字典推导式
print(dic, type(dic))  # {'d': 12, 'c': 11, 'b': 8, 'a': 9} <class 'dict'>
lis = [x for x in range(10)]  # 列表推导式
print(lis, type(lis))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>
gen = (i for i in range(10))  # 生成器
print(gen, type(gen))  # <generator object <genexpr> at 0x7ff5d5e82d58> <class 'generator'>


# 80 字符串长度排序
li1 = ['a', 'bc', 'abc', 'defgh', 'qwer']
print(sorted(li1, key=lambda x: len(x)))  # ['a', 'bc', 'abc', 'qwer', 'defgh']
li1.sort(key=len)
print(li1)  # ['a', 'bc', 'abc', 'qwer', 'defgh']
