

# 1、一行代码实现1--100之和
print(sum(range(101)))


# 2、如何在一个函数内部修改全局变量
a = 100


def foo():
    global a
    a = 200


foo()
print(a)


# 3、列出5个python标准库
'''
math: 数学计算
re: 正则
time/datetime: 时间/日期时间
os: 操作系统相关函数
sys: 命令行参数
'''


# 4、字典如何删除键和合并两个字典
dic1 = {'name': 'zhangsan', 'age': 19, 'gender': 'man'}
dic2 = {'name1': 'lisi', 'age': 20, 'gender1': 'man'}
del dic1['age']  # del
print(dic1)
dic1.update(dic2)  # update
print(dic1)


# 5、谈下python的GIL
'''
GIL 全局解释性锁, 当一个进程有多个线程时 python 解释器会加一把锁, 当线程有耗时操作时
python 会把解释锁打开, 执行下一个进程, 多线程有先后顺序, 并不是同时执行 所以不是真的多线程

多进程资源独立, 有自己的python 解释器, 是真的多进程 但消耗系统资源较大
'''


# 6、python实现列表去重的方法
lst = [1, 2, 3, 4, 3, 2, 3, 4, 2, 6, 5, 7, 9]
a = set(lst)
print(a)  # {1, 2, 3, 4, 5, 6, 7, 9}
print([x for x in a])  # [1, 2, 3, 4, 5, 6, 7, 9]


# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
def foo1(n, *args, **kwargs):
    print(n)
    print('args:', args)  # 以元阻的形式传进来
    print('kwargs:', kwargs)  # 以字典的形式传进来
    for i in args:
        print(i, end=' ')
    print()
    for k, v in kwargs.items():
        print(k, v, end=' ')
    print()


foo1(7, 2, 1, 2, 3, [1, 2, 3], a=99, b=100)


# 8、python2和python3的range（100）的区别
print(range(100))  # py2返回列表 py3返回遗代器, 节约内存


# 9、一句话解释什么样的语言能够用装饰器?
# 函数可以做参数传递的语言, 可以使用装饰品


# 10、python内建数据类型有哪些
'''
int : 整形
bool : 布尔型 
str : 字符串
list : 列表
dict : 字典 
tuple : 元阻
'''
