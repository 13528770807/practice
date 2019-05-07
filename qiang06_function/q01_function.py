def foo(a, b, *, d):  # 可以传带*的参数
    return a+b+d

# printfoo = foo(1, 2, 4)  # error
printfoo = foo(1, 2, d=4)  # "*"以后的参数必须是关键字参数
print(printfoo)


import builtins
print(dir(builtins))  # 内置作用域


matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

# 方法一
list_drived = [[x[i] for x in matrix] for i in range(4)]  # 3*4矩阵列表 转成4*3列表
print(list_drived)

# 方法二
ali = list()
for i in range(4):
    ali.append([row[i] for row in matrix])
print(ali)

# 方法三
ali3 = list()
for i in range(4):
    ali2 = list()
    for x in matrix:
        ali2.append(x[i])
    ali3.append(ali2)
print(ali2)
print(ali3)


# 创建字典
print("="*60)
dic = dict([("zhangqiang", 19), ("lishi", 20), ("wangwu", 21)])  # 构造函数dict()直接从无阻列表中构建字典
print(dic)
dic2 = dict(zhangsan=18, lisi=19, wangwu=20, zhaoliu=21)  # 关键字指定键值对
print(dic2)

# enumerate 获取索引
print("="*60)
for i, x in enumerate(['zhangsan', 'lishi', 'wangwu', 1, 2, 3]):
    print(i, x)


# zip() 同时遍历多个序列
questions = ['name', 'age', 'color']
answer = ['zhangsan', 19, 'blue']
for q, a in zip(questions, answer):
    print("what is your {0}, It is {1}".format(q, a))


# reversed() 反转
for i in reversed(range(1, 10, 2)):
    print(i, end=" ")
print()

# sorted 排序，不修改原值
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
sor = sorted(basket)
print(sor)

for f in sorted(set(basket)):
    print(f)
