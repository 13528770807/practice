# -*- coding: UTF-8 -*-

# 11、简述面向对象中__new__和__init__区别,
'''
__init__ : 初始化方法, 创建对象后就默认被调用了, 可以传参数
1、__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别

2、__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，
可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例

3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，
如果是其他类的类名，；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

'''
import random

# import numpy as np
import re


class Foo(object):
    def __init__(self, color, money):
        self.color = color
        self.money = money

    def move(self):
        print('running.........')


ferrari = Foo('red', '200w')
lawse = Foo('black', '300w')
print('法拉利的顔色为:{},价格{}:'.format(ferrari.color, ferrari.money))
print('劳斯的顔色为:{},价格{}:'.format(lawse.color, lawse.money))


class Obj(object):
    def __init__(self, name, age):
        print('3__init__:', self)  # 3__init__: <__main__.Obj object at 0x7f2e2e100240>
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('1_cls:', id(cls))  # 1_cls: 14915272
        if not hasattr(cls, '_inst'):
            cls._inst = super(Obj, cls).__new__(cls)
            print('2__new__:', cls._inst)  # 2__new__: <__main__.Obj object at 0x7f2e2e100240>
        return cls._inst


a = Obj('zhangsan', 19)
# b = Obj('lisi', 20)
print(a.name, a.age)
# print(b.name, b.age)
print('4_Obj:', id(Obj))  # 4_Obj: 14915272
print('*'*60)


# 12、简述with方法打开处理文件帮我我们做了什么？
"""
打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open

写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，
都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close
"""
f = open('./note.txt', 'wb')
try:
    f.write('hello world')
except:
    pass
finally:
    f.close()

# with open('./note2.txt', 'wb') as f2:
#     f2.write('made in China')


# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
# map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求
li1 = [1, 2, 3, 4, 5]


def foo(x):
    return x ** 2


li2 = list(map(foo, li1))
print(li2)  # [1, 4, 9, 16, 25]
print([x for x in li2 if x > 10])  # [16, 25]
print('='*60)


# 14、python中生成随机整数、随机小数、0--1之间小数方法
print(random.randint(1, 3))
# print(np.random.randn(5))
print(random.random())  # 0.23450313090215458
print('&'*60)


# 15、避免转义给字符串加哪个字母表示原始字符串？
# r , 表示需要原始字符串，不转义特殊字符


# 16、re
str1 = '<div class="name">中国</div>'
res = re.findall(r'<div class=".*">(.*?)</div>', str1)  # .* 类名可有可元, () 提取
print(res)
print("%"*60)


# 17、python 断言方法
n = 3
assert(n > 1)
print('success')  # 打印
# assert(n < 2)
# print('failure')  # 不打印


# 18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
# select distinct name from *;


# 19、10个Linux常用命令
# ls pwd cp mv tar zip unzip lsof grep top tree cat tail herf du cal ssh
# touch mkdir sudo install version pip list cd more echo rm


# 20、python2和python3区别？列举5个,
# name = raw_input('')
# print(name)
# age = input('')
# print(age)
'''
1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')

Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'

2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存

3、python2中使用ascii编码，python中使用utf-8编码

4、python2中unicode表示字符串序列，str表示字节序列

      python3中str表示字符串序列，byte表示字节序列

5、python2中为正常显示中文，引入coding声明，python3中不需要

6、python2中是raw_input()函数，python3中是input()函数

'''