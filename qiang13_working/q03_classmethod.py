import time


class A:
    @classmethod
    def meth(cls):
        x = 1
        print(cls, cls.x)


class B(A):
    x = 2
    pass


B.meth()


class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    # @staticmethod
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)  # 哪个类来调用, 哪个类 cls 来实例化


class Estr(Date):
    def __str__(self):
        return 'year:{}, month:{}, day:{}'.format(self.year, self.month, self.day)
        # return "yesr:%s, month:%s, day:%s" % (self.year, self.month, self.day)


e = Estr.now()  # 类对象Estr.now() 直接调用
print(e)
x = e.now()  # 通过实例e去调用类方法也一样可以使用,静态方法也一样
print(x)


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
a.foo('foo')
a.class_foo('class_foo')
a.static_foo('static_foo')

a.foo(1)
# A.foo(2)  # 类对象调用实例方法会报错
A.foo(a, 2)
A.class_foo(3)  # 类方法由类对象调用
a.class_foo(4)  # 类方法也可由实例对象调用
A.static_foo(5)  # 静态方法可由类对象调用
a.static_foo(6)  # 静态方法也可由实例对象调用


