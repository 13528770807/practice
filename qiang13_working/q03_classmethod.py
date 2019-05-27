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


