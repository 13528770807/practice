

# 11、简述面向对象中__new__和__init__区别,
'''
__new__ :
__init__ : 初始化方法, 创建对象后就默认被调用了, 可以传参数

'''


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
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Obj, cls).__new__(cls)
        return cls._inst


a = Obj('zhangsan', 19)
b = Obj('lisi', 20)
print(a.name, b.age)
print(b.name, b.age)
# f = Foo('yellow', '1000w')
# f.move()

